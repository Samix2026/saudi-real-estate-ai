# برنامج سكني — مصدر البيانات

**الاسم الرسمي:** برنامج سكني  
**الاسم بالإنجليزية:** Sakani Housing Program  
**الموقع الرسمي:** [sakani.com.sa](https://sakani.com.sa)  
**الجهة المشغّلة:** وزارة البلديات والإسكان (Ministry of Municipalities and Housing)

---

## Purpose and Mandate

Sakani is the Saudi government's integrated housing platform and program, launched in 2017 under the Ministry of Municipalities and Housing as part of Vision 2030's housing commitments. It is the primary delivery mechanism for the government's pledge to raise Saudi citizen homeownership from 47% (2016 baseline) to 70% by 2030.

Sakani consolidates multiple housing support streams into a single platform: free land allocations, subsidized ready-built units, and financing coordination with the Real Estate Development Fund (REDF) and partner banks.

---

## Eligibility Criteria

Sakani benefits are available to Saudi citizens who meet the following conditions:
- Saudi national identity card holder
- Has not previously received housing support from a government program
- Does not currently own a residential property (or owns property deemed inadequate)
- Meets income thresholds defined by REDF (varies by program type)
- Registered in the Sakani digital platform (sakani.com.sa)

Family members registered on the national family register may qualify under certain programs.

---

## Types of Support

### 1. Free Land Grants (أراضٍ مجانية)
- Developed residential land plots in government-planned subdivisions
- Served with utilities (water, electricity, roads)
- Citizen builds their own home (may combine with REDF construction loan)
- Available in multiple cities and regions

### 2. Subsidized Ready-Built Units (وحدات سكنية جاهزة)
- Completed apartments and villas in government or developer-built projects
- Priced below market rate, with subsidized financing
- Units allocated through Sakani's queue system based on priority scoring

### 3. REDF Financing Support (دعم صندوق التنمية العقارية)
- Profit rate support: REDF covers the difference between bank commercial rates and a subsidized rate (typically 0% effective rate for qualifying citizens)
- Loan amounts up to SAR 500,000 (subject to REDF policy updates)
- Available through partner banks and directly via REDF

### 4. Monthly Housing Allowance (بدل السكن)
- Cash allowance for citizens on the Sakani waiting list not yet allocated a unit
- Provided while the citizen awaits their housing solution

---

## Vision 2030 Link

Sakani is one of the quantified deliverables of Saudi Arabia's Vision 2030 and the Housing Program (برنامج الإسكان). Annual targets are set for:
- Number of units and land plots allocated
- Total beneficiary families served
- Homeownership rate progress toward 70%

---

## How Developers Participate

Private developers can partner with Sakani to deliver subsidized units:
1. Submit project proposal through the ministry's developer portal
2. Project evaluated against Sakani technical and pricing specifications
3. Approved projects receive guaranteed offtake for subsidized units
4. Developer marketing restricted to Sakani-registered applicants for allocated units

---

## Data Available from Sakani

| Data Type | Access |
|-----------|--------|
| Available land plots by city | Public — sakani.com.sa |
| Ready units listings | Public |
| Citizen application status | Authenticated (citizen login) |
| REDF financing eligibility calculator | Public |
| Waiting list position | Authenticated |

---

## Related Files

- `data/platforms.ar.json` — entry id: `sakani`
- `data/authorities.ar.json` — entry id: `redf` and `moh`
- `data/market-concepts.ar.json` — entry id: `sakani_program`
- `prompts/investor-market-entry.md` — Sakani is government-only; not available to non-Saudi investors

---

> **Disclaimer:** Sakani program eligibility criteria, benefit amounts, and available units change regularly. This documentation reflects publicly available information and may not reflect the current program terms. Always verify current program details at [sakani.com.sa](https://sakani.com.sa) and [redf.gov.sa](https://redf.gov.sa).
