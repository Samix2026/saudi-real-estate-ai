# منصة وافي — مصدر البيانات

**الاسم الرسمي:** منصة وافي لتنظيم البيع على الخارطة  
**الاسم بالإنجليزية:** Wafi — Off-Plan Real Estate Sales Platform  
**الموقع الرسمي:** [wafi.rega.gov.sa](https://wafi.rega.gov.sa)  
**الجهة المشغّلة:** الهيئة العامة للعقار (REGA)

---

## Purpose and Mandate

Wafi is Saudi Arabia's mandatory regulatory platform for off-plan real estate sales (البيع على الخارطة). Launched by REGA in 2017, it governs all residential and commercial real estate projects sold before construction completion. No developer may market, advertise, or accept payments for an off-plan project without first obtaining a Wafi license.

The platform was created in response to a wave of developer defaults in the 2010s that left thousands of Saudi buyers without their purchased units and without recourse. Wafi's escrow and milestone system was designed to structurally prevent a recurrence of this outcome.

---

## How Wafi Works

### 1. Developer Licensing

Before marketing any project, the developer must:
1. Apply for a **Wafi development license** (ترخيص وافي للتطوير العقاري)
2. Submit project plans, permits, and land ownership documentation
3. Demonstrate financial capacity to complete the project
4. Receive REGA approval and a unique project registration number

### 2. Escrow Account (حساب الضمان)

Upon licensing, the developer must open a **dedicated escrow account** at a REGA-approved bank. This account:
- Receives **all buyer payments** directly
- Is operated by an independent escrow agent (not the developer)
- Releases funds to the developer **only upon certified construction milestones** (typically 20%, 40%, 60%, 80%, 100% completion)
- Cannot be withdrawn from for operational expenses unrelated to the project

### 3. Buyer Protections

- **Completion guarantee:** Developer must maintain project completion insurance or provide a bank guarantee
- **Milestone-linked payments:** Payment schedules in sales contracts must align with certified construction progress
- **Buyer cancellation rights:** If the developer delays delivery beyond the contractual date, buyers have the right to cancel and receive full refunds from the escrow account
- **Project monitoring:** REGA-approved engineers inspect and certify each construction milestone

---

## Key Regulation

**نظام التطوير العقاري** — Real Estate Development Law  
Issued by Royal Decree M/24, dated 1443H  
Published in the Official Gazette (أم القرى)

This regulation defines the full legal framework for Wafi, including:
- Developer licensing requirements
- Escrow account rules
- Buyer rights
- Penalties for non-compliance (fines up to SAR 5,000,000 per violation, criminal liability in egregious cases)

---

## Data Available from Wafi

| Data Type | Access |
|-----------|--------|
| Licensed developers list | Public — wafi.rega.gov.sa |
| Registered off-plan projects | Public — searchable by city |
| Project status and completion percentage | Public |
| Escrow bank name per project | Public |
| Developer license status | Public |

---

## Verification Endpoints

To verify a project or developer on Wafi:
- **Check project registration:** wafi.rega.gov.sa/projects
- **Check developer license:** wafi.rega.gov.sa/developers
- Wafi project number format: `W-YYYY-NNNNN`

---

## Using Wafi Data in This Repository

- All entries referencing off-plan projects must include the Wafi project registration number where available
- Developer status (licensed / suspended / expired) changes dynamically — always verify at wafi.rega.gov.sa
- Escrow bank and account status should not be stored as static data; reference the platform for live status
- The `platform` field in `contract-types.ar.json` references wafi for off-plan sale contracts

---

## Related Files

- `data/platforms.ar.json` — entry id: `wafi`
- `data/contract-types.ar.json` — entry id: `off_plan_sale`
- `prompts/off-plan-sale-check.md` — risk analysis prompt referencing Wafi
- `data/market-concepts.ar.json` — entry id: `off_plan_regulatory_framework`

---

> **Disclaimer:** This documentation is for informational purposes only. Wafi platform data and regulations are subject to change. Always verify current developer and project status directly at [wafi.rega.gov.sa](https://wafi.rega.gov.sa).
