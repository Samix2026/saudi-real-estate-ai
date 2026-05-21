# دليل استخدام saudi-real-estate-ai

كيف تستخدم هذا الريبو في مشروعك لبناء تطبيقات عقارية ذكية مستندة للبيانات السعودية الرسمية.

---

## ما الذي يوفره هذا الريبو

| النوع | المحتوى |
|---|---|
| بيانات JSON محققة | 12 dataset، 12 schema، جميعها valid |
| مصطلحات | 83 مصطلح عقاري ثنائي اللغة |
| System Prompts | 5 قوالب جاهزة للاستخدام (مستأجر، مالك، مستثمر، وسيط، مطور) |
| أمثلة Q&A | 20 سؤال وجواب حقيقي (4 لكل جمهور) |
| مصادر موثقة | روابط لجميع الجهات الرسمية السعودية |

**ما لا يوفره:** بيانات الأسعار الحية، مخزون الوحدات المتاحة، بيانات صناديق REIT الحية.

---

## خيار 1: RAG — Retrieval-Augmented Generation

الأنسب لبناء chatbot أو assistant يُجيب على أسئلة حرة.

**الفكرة:** حمِّل الـ JSON files في vector store، واسترجع المقاطع ذات الصلة عند كل سؤال، وأرسلها مع السؤال إلى LLM.

```python
import json

# تحميل dataset
with open('data/real-estate-terms.ar.json', 'r', encoding='utf-8') as f:
    terms = json.load(f)

# فلترة حسب الجمهور
tenant_terms = [t for t in terms if 'مستأجر' in t.get('audience', [])]

# فلترة حسب الفئة
contract_terms = [t for t in terms if t.get('category') == 'عقود']

# بناء نص للـ embedding
def term_to_text(term):
    return f"{term['name_ar']} ({term['name_en']}): {term['definition_ar']}"

texts = [term_to_text(t) for t in tenant_terms]
```

**الـ datasets الأكثر فائدة لـ RAG:**

| Dataset | الحجم | الاستخدام الأمثل |
|---|---|---|
| `real-estate-terms.ar.json` | 83 مصطلح | فهم المصطلحات في الأسئلة |
| `contract-types.ar.json` | 8 عقود | أسئلة عن أنواع العقود |
| `property-types.ar.json` | 15 نوع | أسئلة عن أنواع العقارات |
| `saudi-building-code.ar.json` | SBC كامل | أسئلة عن البناء والضمانات |
| `reits-framework.ar.json` | 10 مفاهيم | أسئلة عن الاستثمار في REITs |
| `housing-programs.ar.json` | 7 برامج | أسئلة عن برامج الدعم السكني |

---

## خيار 2: System Prompt مع Context مُضمَّن

الأنسب للتطبيقات التي تعرف جمهورها مسبقاً.

**الفكرة:** اختر System Prompt بحسب المستخدم، وأضف محتوى الـ JSON المرتبط كـ context داخل الـ system message.

```python
import json

def build_system_prompt(audience: str) -> str:
    # قراءة system prompt الجاهز
    prompt_map = {
        'tenant': 'prompts/system-prompts/tenant.md',
        'owner': 'prompts/system-prompts/owner.md',
        'investor': 'prompts/system-prompts/investor.md',
        'broker': 'prompts/system-prompts/broker.md',
        'developer': 'prompts/system-prompts/developer.md',
    }

    with open(prompt_map[audience], 'r', encoding='utf-8') as f:
        base_prompt = f.read()

    # إضافة البيانات المرتبطة بهذا الجمهور
    relevant_data = load_audience_data(audience)

    return base_prompt + "\n\n## البيانات المرجعية\n" + json.dumps(
        relevant_data, ensure_ascii=False, indent=2
    )


def load_audience_data(audience: str) -> dict:
    data = {}
    audience_files = {
        'tenant':    ['contract-types', 'platforms', 'real-estate-terms'],
        'owner':     ['contract-types', 'platforms', 'property-types', 'saudi-building-code'],
        'investor':  ['foreign-investor', 'reits-framework', 'housing-programs', 'property-types'],
        'broker':    ['broker-requirements', 'contract-types', 'platforms'],
        'developer': ['saudi-building-code', 'platforms', 'property-types', 'property-coding'],
    }
    for filename in audience_files.get(audience, []):
        with open(f'data/{filename}.ar.json', 'r', encoding='utf-8') as f:
            data[filename] = json.load(f)
    return data
```

---

## خيار 3: MCP Server (قادم في Phase 4)

سيُتيح ربط الريبو مباشرةً بـ Claude Desktop كأداة (tool) قابلة للاستدعاء.
كل dataset سيصبح tool مستقل: `search_terms()`, `get_property_types()`, `get_housing_programs()`, إلخ.

---

## اختيار الـ System Prompt الصحيح

| الجمهور | الملف |
|---|---|
| مستأجر | `prompts/system-prompts/tenant.md` |
| مالك | `prompts/system-prompts/owner.md` |
| مستثمر | `prompts/system-prompts/investor.md` |
| وسيط عقاري | `prompts/system-prompts/broker.md` |
| مطور عقاري | `prompts/system-prompts/developer.md` |
| مستثمر أجنبي (تفصيلي) | `prompts/investor-market-entry.md` |

---

## الـ Datasets المناسبة لكل جمهور

| الجمهور | الملفات الأساسية | الملفات الثانوية |
|---|---|---|
| مستأجر | contract-types, platforms, real-estate-terms | property-types |
| مالك | contract-types, platforms, property-types | saudi-building-code, property-coding |
| مستثمر سعودي | housing-programs, reits-framework, property-types | real-estate-terms |
| مستثمر أجنبي | foreign-investor, reits-framework, property-types | real-estate-terms |
| وسيط | broker-requirements, contract-types, platforms | real-estate-terms |
| مطور | saudi-building-code, platforms, property-types | property-coding, housing-programs |

---

## الـ Schema Validation

تحقق من صحة البيانات قبل استخدامها في الإنتاج:

```bash
python3 scripts/validate-data.py
# أو بتفاصيل الأخطاء:
python3 scripts/validate-data.py --verbose
```

---

## نموذج استخدام كامل (Claude API)

```python
import anthropic
import json

client = anthropic.Anthropic()

def ask_real_estate_question(question: str, audience: str) -> str:
    system_prompt = build_system_prompt(audience)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": question}]
    )
    return message.content[0].text


# مثال:
answer = ask_real_estate_question(
    question="كيف أسجل عقد إيجاري في منصة إيجار؟",
    audience="tenant"
)
print(answer)
```

---

## تحذير مهم

هذا الريبو مصدر معرفة ثابتة — **لا يُشغِّل استعلامات حية**.

البيانات التالية تحتاج مصادر خارجية منفصلة:

- أسعار الإيجار والبيع الحالية
- مخزون الوحدات المتاحة
- بيانات صناديق REIT الحية (تداول API)
- مشاريع سكني الحية ومواعيد التسليم
- بيانات السجل العقاري الحي (ريدز)
