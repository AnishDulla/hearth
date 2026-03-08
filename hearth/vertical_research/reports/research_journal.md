# Research Journal

## 2026-03-06 13:21:21 | PI law firms | $10M-$250M annual revenue

### Durable Findings
- Intake (lead capture)
- Qualification/Retention
- Treatment tracking (pre-lit)
- Medical records and bills acquisition
- Demand package creation (pre-suit)

### Strongest Pain Signals
- Missed/slow intake follow-up causes lead leakage
- 30–60+ day delays to obtain complete medical records and bills
- Demand drafting backlog and inconsistent valuation
- Heavy inbound status calls and treatment drop-offs
- Lien resolution and trust disbursement delays post-settlement

### Strongest Tech Stack Findings
- PI case management platforms: Filevine, Litify, SmartAdvocate
- Intake/lead management & call tracking: Lead Docket (Filevine), Captorra, CallRail
- Client communication & texting: Case Status, Kenect, RingCentral texting
- Medical records/bills retrieval (ROI): ChartRequest, Sharecare HDS, Compex
- Demand drafting and valuation: EvenUp, Filevine Demands.ai, Internal templates

### Candidate AI Use Cases
- #1 AI medical record ingestion → chronology + specials extraction
- #2 AI-assisted demand package drafting with valuation benchmarks
- #3 AI-driven intake triage, follow-up, and e-sign orchestration

### Open Questions
- Quantify current demand backlog (cases waiting on drafts) and redline cycles per demand
- Provider-specific ROI SLAs (by health system) and denial rates driving rework
- After-hours lead volumes and conversion vs. business hours
- Lien resolution median days by payer (Medicare vs Medicaid vs ERISA) in this ICP

### Contradictions / Uncertain Claims
- Per-case time savings for AI chronology (4–8 hours) and demand drafting throughput (2–3x) are inferred from role task analyses and vendor positioning; require firm-specific baselining
- Economic impact of intake lift (3–10%) depends on lead mix and attorney acceptance criteria

## 2026-03-06 14:44:13 | real estate brokerages | $5M-$50M annual revenue

### Durable Findings
- Lead capture and routing
- Listing acquisition (seller side)
- Buyer pipeline and showings
- Offer writing and acceptance
- Transaction coordination and compliance (contract-to-close)

### Strongest Pain Signals
- Slow/uneven speed-to-lead and missed lead SLAs
- Duplicate data entry across MLS, CRM, transaction and back office
- Compliance document chase and file readiness for audit
- Commission miscalculations on complex plans (caps, teams, referrals, franchise fees)
- CDA errors or timing issues causing delayed or misdirected payments

### Strongest Tech Stack Findings
- Front office CRM/IDX/Lead routing: kvCORE (Inside Real Estate; integrated with Brokermint back office), Follow Up Boss, BoomTown
- Transaction management, forms, e-sign, compliance: Lone Wolf Transactions (zipForm Edition), SkySlope (with DigiSign, Smart Assist, Auto-Split & Assign), dotloop
- Back office: commissions, trust accounting, billing, reporting: Lone Wolf Back Office (formerly brokerWOLF), Brokermint (Inside Real Estate), iBroker + QuickBooks Online
- Showings and access: ShowingTime+ (MLS-integrated scheduling, feedback), Supra eKEY / Sentrilock
- Listing syndication: ListHub, IDX feeds to broker/team sites

### Candidate AI Use Cases
- #1 Automated compliance QA and document orchestration
- #2 Commission plan validation and CDA anomaly detection
- #3 Lead response copilot (speed-to-lead and re-routing)

### Open Questions
- Quantify actual CDA reissue rates and payout error incidence by brokerage size and plan complexity.
- Map specific MLS/CRM/TM integration gaps across the brokerage’s MLSs to prioritize double-entry elimination.
- Validate agent adoption levers (e.g., tying faster pay or lead priority to compliance behaviors) within the brokerage’s culture.
- Measure current median first-response time and routing fairness to calibrate AI copilot ROI.

### Contradictions / Uncertain Claims
- Agent counts for $5M–$50M brokerages typically range 50–400 depending on average GCI per agent and split economics. Not directly cited, inferred from industry norms.
- Time savings percentages in compliance QA (30–50%) are estimated based on manual steps eliminated (PDF splitting, missing-doc chase) and vendor positioning; would need time-and-motion validation.
- Lead response conversion lift (20–40%) reflects ranges reported in industry playbooks; exact lift varies by source/market.

## 2026-03-06 15:10:04 | opportunities | real estate brokerages | $5M-$50M annual revenue

- top_ai_use_cases: 3 items

## 2026-03-06 19:15:16 | P&C insurance | $5M-$50M annual revenue

### Durable Findings
- 1. Lead generation and prospecting
- 2. Intake and appetite check
- 3. Quoting and submissions
- 4. Proposal and binding
- 5. Policy issuance and policy checking

### Strongest Pain Signals
- Duplicate data entry across AMS, raters, ACORDs, and carrier portals
- High-volume COI issuance with contract-specific requirements; frequent reissuance after endorsements/renewals
- Manual policy checking of decs/endorsements vs proposal/expiring
- Small commercial submissions still require multiple portals and underwriter back-and-forth
- Direct-bill commission reconciliation and suspense cleanup

### Strongest Tech Stack Findings
- Agency Management Systems (AMS): Applied Epic, Vertafore AMS360, EZLynx Management System
- Carrier connectivity (IVANS): IVANS Download (policy, claims, eDocs/Messages), IVANS Market Appetite
- Comparative rating & small commercial quoting: EZLynx Rating Engine (PL), PL Rating (Vertafore), ITC TurboRater
- Submission/app collection (Commercial): Indio (Epic bi-directional), Zywave (forms)
- Certificates of Insurance (COI) issuance/tracking: AMS certificate modules, Certificial (Smart COI), TrustLayer/myCOI (holder tracking)

### Candidate AI Use Cases
- #1 AI-driven COI automation: read requirements, validate coverage, and auto-issue/reissue
- #2 AI policy checking and endorsement reconciliation
- #3 AI service inbox triage-to-action (endorsements, COIs, billing, FNOL)

### Open Questions
- Confirm COI volume and paid vs unpaid mix per agency vertical (e.g., construction vs other).
- Quantify baseline time for manual policy checks by LOB in target agencies (to size ROI precisely).
- Map exact carrier/LOB integration coverage in current stack (Tarmika/Semsee/Bold Penguin) to identify rekeying pockets.
- Assess accounting exception drivers in DBCS (by top carriers) to target reconciliation automation rules.
- Validate appetite search behavior: extent of IVANS Market Appetite vs underwriter relationships usage in practice.

### Contradictions / Uncertain Claims
- Exact per-transaction minutes saved for COI issuance and endorsement processing in this specific ICP; ranges provided from industry practice and vendor claims.
- Share of carriers per agency supporting claims download; noted as inconsistent but varies by carrier mix.
- Average FTE count and policy count bands for $5M–$50M agencies; typical ranges inferred from operating patterns.

## 2026-03-07 10:01:04 | home services | $5M-$50M annual revenue

### Durable Findings
- Lead capture and call booking
- Online booking and confirmations
- Dispatch and capacity planning
- Onsite diagnosis and sales presentation
- Job execution and documentation

### Strongest Pain Signals
- Missed/abandoned inbound calls, especially at peaks and after-hours
- Low-quality marketplace leads (shared/double-sold, poor contactability)
- Scheduling gaps from cancellations/no-shows
- Inefficient routing and skill mismatches increase drive time and re-dispatch
- Out-of-date pricebook and supplier costs causing margin leakage

### Strongest Tech Stack Findings
- Field Service Management (FSM)/CRM: ServiceTitan, Housecall Pro, Jobber
- Telephony/call tracking/contact center: ServiceTitan Phones Pro/Contact Center Pro, CallRail, RingCentral
- Online booking and reminders: ServiceTitan Scheduling Pro (Schedule Engine), Reserve with Google (via ServiceTitan), Housecall Pro/Jobber online booking
- Payments and consumer financing: ServiceTitan Payments (Tap to Pay), Jobber Payments, Housecall Pro Payments
- Procurement, inventory, AP automation: ServiceTitan Purchasing & Inventory + Ferguson integration (real-time pricing/availability, in-app POs), QuickBooks, ServiceTitan AP Automation (AI bill-to-PO/job match)

### Candidate AI Use Cases
- #1 AI call answering + booking assistant (24/7), integrated to FSM
- #2 AI dispatch and dynamic capacity optimizer
- #3 AI pricebook + margin guard (auto-cost sync, pricing suggestions, quote risk alerts)

### Open Questions
- Quantify actual no-show and cancellation rates by sub-trade and season for target firms.
- Measure field documentation time and callback rates before/after structured prompts/AI transcriptions.
- Validate realized AP automation time savings and error reduction with Controller/AP teams in this ICP.
- Pricebook governance cadence and the degree of existing supplier integrations in the target installed base.

### Contradictions / Uncertain Claims
- Exact missed-call rates for a given $5–$50M shop vary; we used 10–20% range based on CallRail home services (14%) vs SMB overall (30%).
- Revenue/tech lift from dispatch optimization estimated from industry routing improvements (10–20% drive-time reduction) rather than a single benchmark tied to this ICP.
- Gross margin leakage of 2–4 pts from outdated pricebooks is based on operator anecdotes and supplier price volatility; precise point estimates vary by trade and season.

