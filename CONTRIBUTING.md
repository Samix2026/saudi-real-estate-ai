# Contributing to saudi-real-estate-ai | المساهمة في saudi-real-estate-ai

---

## English

Thank you for your interest in contributing to `saudi-real-estate-ai`. This project is a structured knowledge base for Saudi Arabia's real estate sector, designed for AI agent and developer consumption. All contributions must be traceable to official Saudi government sources.

### Guiding Principles

1. **No fabricated data.** Every entry you add to a data file must have a `source_url` pointing to an official Saudi government page (rega.gov.sa, ejar.sa, wafi.rega.gov.sa, sakani.com.sa, moh.gov.sa, zatca.gov.sa, or similar authorities). Third-party summaries are not acceptable as primary sources.
2. **No placeholders.** Never use `TBD`, `N/A`, `unknown`, or similar values in required fields. Omit optional fields instead.
3. **Bilingual consistency.** If you update an Arabic file, update the corresponding English file in the same pull request. Arabic and English descriptions of the same concept must be equivalent in meaning.
4. **Modern Standard Arabic.** Arabic content must use MSA with authentic Saudi real estate terminology as used by REGA, ejar, wafi, and sakani. Do not translate technical terms loosely.
5. **Validation must pass.** Run `python scripts/validate-data.py` before submitting any data changes. Do not open a pull request if validation fails.

### What We Need

The following areas are actively seeking contributions:

- **`data/real-estate-terms.ar.json`** — Additional terms from official REGA and ejar publications, especially for commercial real estate, NEOM/giga-project zones, and property management.
- **`data/broker-requirements.ar.json`** — Updates as REGA issues new licensing circulars or CPD hour requirements.
- **`data/foreign-investor.ar.json`** — Updates when MISA or REGA issue amended foreign ownership regulations.
- **`data/authorities.ar.json`** — Additional regulatory bodies (e.g., municipality-level bodies, specialized courts).
- **`prompts/`** — New system prompt templates for use cases not yet covered (e.g., property management Q&A, off-plan buyer guidance).
- **`examples/`** — Additional worked examples in Arabic and English demonstrating how to use the prompts with realistic scenarios.
- **Schema improvements** — Backward-compatible additions to existing schemas (open an issue before changing schemas).

### How to Contribute

**Step 1 — Open an issue first.**
Before writing any code or data, open a GitHub issue describing what you intend to add or change. This prevents duplicate work and lets maintainers confirm the source is acceptable before you invest time.

**Step 2 — Fork and branch.**
Fork the repository and create a feature branch with a descriptive name:
```
git checkout -b add/real-estate-term-ijar-tamliki
```

**Step 3 — Add your changes.**
Follow the dataset standards in `CLAUDE.md` exactly. Ensure:
- `id` is snake_case and unique within the file
- `source_url` points to an official government page (not a news article or blog)
- `last_verified` is today's date in ISO 8601 format (`YYYY-MM-DD`)
- All required fields are populated with real data

**Step 4 — Run validation.**
```bash
pip install jsonschema
python scripts/validate-data.py
```
All datasets must show `✓` before you open a pull request.

**Step 5 — Open a pull request.**
Reference the issue number in the PR description. Fill in the PR template explaining:
- What you added or changed
- The official source URL confirming the data
- The date you verified the source

### Reporting Errors

If you find an entry with an incorrect URL, outdated information, or a factual error:
1. Open an issue with the label `data-error`
2. Include the `id` of the incorrect entry, the file name, and a link to the correct official source
3. Do not submit corrections without a source citation

### Acceptance Criteria

A contribution will be accepted when it meets all of the following:
- All required fields are populated with real, source-backed data
- `python scripts/validate-data.py` passes with no failures
- The official source URL is reachable and confirms the data
- Arabic content uses MSA with correct Saudi real estate terminology
- Bilingual files are updated together in the same commit

---

## العربية

شكراً لاهتمامك بالمساهمة في `saudi-real-estate-ai`. هذا المشروع قاعدة معرفية منظمة لقطاع العقارات في المملكة العربية السعودية، مُصممة لاستخدام وكلاء الذكاء الاصطناعي والمطورين. يجب أن تكون جميع المساهمات قابلة للتتبع إلى مصادر حكومية سعودية رسمية.

### المبادئ الأساسية

1. **لا بيانات مخترعة.** يجب أن يتضمن كل إدخال تُضيفه إلى ملف البيانات رابطاً (`source_url`) يُشير إلى صفحة رسمية في موقع حكومي سعودي (rega.gov.sa أو ejar.sa أو wafi.rega.gov.sa أو sakani.com.sa أو moh.gov.sa أو zatca.gov.sa أو ما شابهها). الملخصات الصادرة عن جهات غير رسمية غير مقبولة كمصادر أولية.
2. **لا حقول فارغة أو احتياطية.** لا تستخدم `TBD` أو `N/A` أو `غير محدد` أو ما يماثلها في الحقول الإلزامية. احذف الحقول الاختيارية إن لم تتوفر لها قيمة.
3. **التوازي اللغوي.** إذا حدّثت ملفاً بالعربية، حدّث الملف الإنجليزي المقابل في طلب السحب ذاته.
4. **العربية الفصحى الرسمية.** يجب أن يستخدم المحتوى العربي المصطلحات العقارية السعودية الرسمية كما وردت في وثائق الهيئة العامة للعقار وإيجار ووافي وسكني.
5. **يجب نجاح التحقق.** شغّل `python scripts/validate-data.py` قبل تقديم أي تغييرات في ملفات البيانات.

### مجالات تحتاج مساهمات

- **`data/real-estate-terms.ar.json`** — مصطلحات إضافية من منشورات الهيئة العامة للعقار وإيجار، ولا سيما للعقارات التجارية ومناطق مشاريع الرؤية الكبرى.
- **`data/broker-requirements.ar.json`** — تحديثات عند إصدار الهيئة العامة للعقار تعاميم ترخيص جديدة.
- **`data/foreign-investor.ar.json`** — تحديثات عند صدور تعديلات على أنظمة تملك الأجانب من الهيئة العامة للعقار أو وزارة الاستثمار.
- **`prompts/`** — قوالب موجّهات نظام جديدة لحالات غير مغطاة بعد.
- **`examples/`** — أمثلة عملية إضافية باللغتين العربية والإنجليزية.

### خطوات المساهمة

**الخطوة 1 — افتح قضية (issue) أولاً.**
قبل كتابة أي بيانات أو كود، افتح قضية في GitHub تصف ما تنوي إضافته أو تعديله. هذا يمنع تكرار العمل ويُمكّن المشرفين من التحقق من المصدر قبل أن تستثمر وقتك.

**الخطوة 2 — شوّك المستودع وأنشئ فرعاً.**
شوّك المستودع وأنشئ فرعاً بمسمى وصفي:
```
git checkout -b add/real-estate-term-ijar-tamliki
```

**الخطوة 3 — أضف تغييراتك.**
اتبع معايير مجموعات البيانات في `CLAUDE.md` بدقة.

**الخطوة 4 — شغّل التحقق.**
```bash
pip install jsonschema
python scripts/validate-data.py
```
يجب أن تُظهر جميع مجموعات البيانات `✓` قبل فتح طلب السحب.

**الخطوة 5 — افتح طلب سحب (Pull Request).**
أشر إلى رقم القضية في وصف طلب السحب، مع ذكر المصدر الرسمي الذي يؤكد البيانات وتاريخ التحقق.

### الإبلاغ عن أخطاء

إذا وجدت إدخالاً يحتوي على رابط غير صحيح أو معلومات قديمة:
1. افتح قضية بتسمية `data-error`
2. ضمّن `id` الإدخال الخاطئ واسم الملف ورابط المصدر الرسمي الصحيح
3. لا تُقدم تصحيحات دون استشهاد بمصدر

### معايير قبول المساهمة

تُقبل المساهمة عند استيفاء جميع ما يلي:
- جميع الحقول الإلزامية مكتملة ببيانات حقيقية مدعومة بمصادر
- نجاح `python scripts/validate-data.py` دون أي إخفاقات
- رابط المصدر الرسمي صالح ويؤكد البيانات
- المحتوى العربي يستخدم الفصحى بالمصطلحات العقارية السعودية الصحيحة
- الملفات ثنائية اللغة محدَّثة معاً في الالتزام ذاته

---

> هذا المحتوى لأغراض معلوماتية فقط ولا يُعدّ استشارة قانونية أو مالية. تحقق دائمًا من المتطلبات الحالية عبر الجهات السعودية الرسمية (هيئة العقار، إيجار، وافي، سكني) واستشر متخصصين عقاريين سعوديين مرخَّصين قبل اتخاذ أي قرارات قانونية أو مالية.
>
> This content is for informational purposes only and does not constitute legal or financial advice. Always verify through official Saudi authorities (REGA, ejar, wafi, sakani) and consult licensed Saudi real estate professionals before making any legal or financial decisions.
