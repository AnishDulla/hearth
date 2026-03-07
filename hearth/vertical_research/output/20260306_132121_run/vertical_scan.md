# vertical_scan

## Narrative Synthesis
vertical='Personal Injury (PI) law firms' icp=ICPProfile(revenue_range='$10M–$250M', firm_archetypes=['High-volume PI settlement firms with centralized intake and pre-litigation teams (multi-state advertising-driven)', 'Boutique PI trial firms with lower intake volume but higher case values and deeper litigation benches', 'Regional PI platforms rolling up solo/small practices onto a common operating stack'], buyer_roles=['Managing Partner/Owner', 'COO/Director of Operations', 'Intake Director/Marketing Director', 'Pre-Litigation Director', 'Litigation Managing Attorney', 'CFO/Controller (trust/IOLTA oversight)', 'IT/Systems Admin'], operating_characteristics=['Contingency-fee model; cash conversion dependent on cycle time from incident to disbursement', 'Marketing-heavy funnels (phone/web leads) → centralized intake → pre-lit case building → demand/negotiation → litigation if needed → settlement → lien resolution/disbursement', 'Matter-centric operations with strict deadline tracking (SOL, discovery) and statutory compliance (HIPAA record access windows; Medicare secondary payer rules)', 'Heavy use of PI-specific case management platforms (Filevine, Litify, SmartAdvocate, CASEpeer, Assembly Neos) with integrated intake, e-sign, records retrieval, texting, analytics', 'Staffing by role: intake specialists, case managers, paralegals, demand writers, negotiators (pre-lit adjuster-facing), litigators, lien/settlement coordinators']) workflow_map=[WorkflowStage(stage='Intake (lead capture)', owner_roles=['Intake specialists', 'Intake manager', 'Marketing/Call tracking admin'], current_process='Inbound calls/web forms/chat; capture facts (incident date, venue, injuries, at-fault, coverage), conflict check, schedule attorney callback; push to lead/intake system; rapid e-sign of retainer/authorizations if qualified.', common_tools=['Lead Docket (Filevine)', 'Captorra', 'CallRail (call tracking/AI voice)', 'Kenect (texting)', 'Ngage/chat', 'Vinesign/DocuSign for e-sign'], manual_steps=['Manual speed-to-lead call-backs and re-attempts', 'Eligibility scripts executed by agents', 'Manual conflict check in DMS/CRM', 'After-hours coverage via answering services'], pain_points=['Missed/slow response to high-intent calls', 'Inconsistent qualification and documentation', 'After-hours leakage', 'Fragmented comms (phone/text/email)'], why_painful='PI revenue is intake-constrained; lost or delayed contacts convert elsewhere; inconsistent triage admits weak cases and wastes downstream capacity.', business_impact='Lead leakage and variable quality reduce signed retainers; marketing ROI deteriorates; downstream caseload volatility. Captorra markets +27% captured clients through structured intake and follow-up; call tracking/24x7 agents aim to reduce missed calls.'), WorkflowStage(stage='Qualification/Retention', owner_roles=['Intake specialists', 'Attorneys (screening)'], current_process='Confirm case criteria, venue/SOL window, policy limits where known; obtain signed retainer, HIPAA and records/bills authorizations via e-sign; open matter in case system.', common_tools=['Lead Docket ↔ Filevine', 'Litify intake', 'Vinesign/DocuSign'], manual_steps=['Attorney review of borderline cases', 'Chasing signatures by phone/text/email'], pain_points=['Signature chase delays', 'Borderline-case backlogs'], why_painful='Delay increases client shopping risk; SOL risk for late-filed claims.', business_impact='Lower conversion on qualified leads; escalated attorney time on admin review.'), WorkflowStage(stage='Treatment tracking (pre-lit)', owner_roles=['Case managers', 'Paralegals'], current_process='Track providers, appointments, and Maximum Medical Improvement (MMI); ensure treatment continuity; log specials (medical bills) and wage loss; client updates via calls/text/app.', common_tools=['Filevine/CASEpeer/SmartAdvocate treatment modules', 'Case Status (client mobile updates)', 'Kenect texting'], manual_steps=['Provider scheduling nudges', 'Manual bill tallying in spreadsheets', 'Frequent status calls'], pain_points=['Treatment gaps and missed appointments', 'High inbound status-call load', 'Manual specials tracking'], why_painful='Gaps devalue cases; staff time diverted to repetitive updates (Case Status claims ~50% fewer inbound calls with app-based updates).', business_impact='Lower settlement value; staff productivity loss; client churn risk.'), WorkflowStage(stage='Medical records and bills acquisition', owner_roles=['Case managers', 'Records team', 'Paralegals'], current_process='Submit HIPAA-compliant requests to providers; chase status; receive records; organize and upload; request itemized bills and liens.', common_tools=['ChartRequest/Sharecare/Compex/YoCierge (ROI)', 'SmartAdvocate–Compex integration', 'Filevine docs'], manual_steps=['Authorization QC; fax/portal submissions; follow-ups; appeal denials; reconcile multiple custodians'], pain_points=['Cycle time is long and variable; denials for technical errors; volume of follow-ups'], why_painful='HIPAA allows 30 days to respond (one 30-day extension); vendors report ~30-day averages—delays stall demand drafting and negotiation.', business_impact='Adds 30–60+ days to case readiness; increases admin labor; evidence gaps weaken demands.'), WorkflowStage(stage='Demand package creation (pre-suit)', owner_roles=['Demand writers', 'Paralegals', 'Attorneys (review)'], current_process='Compile liability narrative, med chronology/digests, bills/specials, damages model, photos/police report; draft demand letter and supporting exhibits; quality review; send to carrier.', common_tools=['EvenUp (AI demand packages)', 'Filevine Demands.ai', 'CaseMetrix (valuation comps)', 'Word/PDF templates'], manual_steps=['Manual med chronology and damages modeling', 'Iterative edits among writer/attorney', 'Evidence/bill reconciliation'], pain_points=['Backlog in drafting; inconsistency in valuation and narrative quality; error-prone bill totals'], why_painful='Delays push negotiation start; inconsistent quality depresses offers; attorney review time heavy.', business_impact='Adds weeks; lower opening offers; reduced throughput per FTE.'), WorkflowStage(stage='Negotiation (pre-lit)', owner_roles=['Negotiators', 'Attorneys', 'Paralegals'], current_process='Submit demand; insurer review; counteroffers; provide supplements; mediate as needed; if impasse, file suit to preserve SOL.', common_tools=['Email/carrier portals', 'CaseMetrix comps', 'Matter management reminders for SOL'], manual_steps=['Phone negotiations; compiling supplements; scheduling mediation'], pain_points=['Slow insurer response; weak comps; SOL pressure'], why_painful='Negotiation windows typically 30–90 days post-demand; poor comps reduce leverage.', business_impact='Prolonged cycle time; higher suit rates when leverage is weak.'), WorkflowStage(stage='Litigation', owner_roles=['Attorneys', 'Litigation paralegals'], current_process='File and serve; discovery, depositions, expert work; mediation; trial if necessary; many settle post-filing.', common_tools=['Litify/Filevine/SmartAdvocate for deadlines', 'eDiscovery repositories as needed'], manual_steps=['Calendar/deadline management', 'Drafting/discovery exchange', 'Scheduling'], pain_points=['Court-driven delays; discovery burdens; deadline risk'], why_painful='Timelines extend several months to 2+ years depending on venue and complexity.', business_impact='Capital tied up; higher costs; burnout risk.'), WorkflowStage(stage='Settlement, liens, and disbursement', owner_roles=['Lien coordinators', 'Settlement coordinators', 'CFO/Accounting'], current_process='Confirm settlement terms; identify and resolve liens (Medicare/Medicaid/ERISA/provider); receive funds to trust; calculate fees/costs/client net; generate closing statements; pay liens; disburse client funds; perform trust reconciliations.', common_tools=['SmartAdvocate disbursements module', 'Synergy/Compass (lien services)', 'Trust accounting (CosmoLex/QuickBooks + trust add-ons)', 'State bar IOLTA resources'], manual_steps=['Medicare conditional payment disputes; provider negotiations; check cutting; three-way trust reconciliations monthly'], pain_points=['Lien resolution delays (Medicare final demands post-settlement); reconciliation complexity; uncashed checks follow-up'], why_painful='CMS conditional payment/final demand requirements add weeks; strict trust procedures create admin load; errors are sanction risks.', business_impact='Delays revenue recognition; compliance exposure; client dissatisfaction if disbursement lags.')] technology_map=[TechnologyCategory(category='PI case management platforms', likely_vendors=['Filevine', 'Litify', 'SmartAdvocate', 'CASEpeer', 'Assembly Neos'], job_to_be_done='End-to-end matter, workflow, deadlines, docs, comms, reporting for PI.', where_it_breaks='Customization debt; siloed intake vs demand drafting; record retrieval not native; analytics limited without BI.', human_workarounds=['Spreadsheets for specials and KPIs', 'Email/phone status updates', 'Manual deadline audits']), TechnologyCategory(category='Intake/lead management & call tracking', likely_vendors=['Lead Docket (Filevine)', 'Captorra', 'CallRail', 'Ngage live chat'], job_to_be_done='Capture, qualify, route, and sign clients quickly; attribute marketing; reduce missed calls.', where_it_breaks='After-hours responsiveness; inconsistent scripts; fragmented comms channels; limited AI triage.', human_workarounds=['Answering services', 'Manual call-backs', 'Ad hoc follow-ups via personal phones']), TechnologyCategory(category='Client communication & texting', likely_vendors=['Case Status', 'Kenect', 'RingCentral texting'], job_to_be_done='Lower inbound status calls; structured updates; reviews capture.', where_it_breaks='Client adoption varies; duplicate channels persist; content not personalized to stage.', human_workarounds=['Broadcast texts', 'Mass email updates', 'Phone trees']), TechnologyCategory(category='Medical records/bills retrieval (ROI)', likely_vendors=['ChartRequest', 'Sharecare HDS', 'Compex', 'YoCierge'], job_to_be_done='HIPAA-compliant requests, tracking, and delivery of records/bills.', where_it_breaks='Provider delays; denials for authorizations; multiple custodians; fee disputes.', human_workarounds=['Fax + phone chases; portal uploads; manual ticklers']), TechnologyCategory(category='Demand drafting and valuation', likely_vendors=['EvenUp', 'Filevine Demands.ai', 'Internal templates', 'CaseMetrix (comps)'], job_to_be_done='Create persuasive, accurate demand packages; benchmark value; standardize quality.', where_it_breaks='Manual chronology; error-prone specials; uneven narrative; limited comps outside certain regions.', human_workarounds=['Freelance demand writers', 'Attorney-heavy edits', 'Informal peer comps']), TechnologyCategory(category='Lien resolution & settlement admin', likely_vendors=['Synergy', 'Compass', 'In-house lien teams'], job_to_be_done='Identify, audit, negotiate, and resolve statutory and provider liens; ensure Medicare compliance; speed disbursement.', where_it_breaks='Opaque payer timelines; manual status checks; document-heavy disputes.', human_workarounds=['Phone/fax with BCRC/carriers/providers; spreadsheet trackers']), TechnologyCategory(category='Trust/IOLTA accounting & disbursement', likely_vendors=['CosmoLex', 'TrustBooks', 'QuickBooks + procedures', 'State Bar resources (WSBA, Florida Bar)'], job_to_be_done='Compliant trust accounting, three-way reconciliation, settlement statements, check cutting/ACH.', where_it_breaks='Manual reconciliation and settlement waterfalls; integration gaps with case systems.', human_workarounds=['Manual three-way monthly reconciliation; journal entries; paper checks'])] pain_point_map=[PainPoint(pain='Missed/slow intake follow-up causes lead leakage', who_feels_it=['Intake specialists', 'Intake manager', 'Managing Partner'], where_in_workflow='Intake', why_it_persists='After-hours coverage gaps; no SLA dashboards; fragmented phone/text/email systems.', current_workaround='Answering services; ad hoc call-backs; manual spreadsheets for follow-ups.', why_workaround_fails='Inconsistent; no attribution/QA; poor client experience.', severity='high', frequency='daily', economic_impact='Each 1% improvement in signed retainer rate on a 5,000-lead/year funnel can add tens of cases and $500k–$1M+ lifetime fee revenue depending on case mix (inferred). Captorra markets +27% capture with structured intake.'), PainPoint(pain='30–60+ day delays to obtain complete medical records and bills', who_feels_it=['Case managers', 'Paralegals', 'Demand writers'], where_in_workflow='Medical records/bills acquisition', why_it_persists='HIPAA permits 30 days + one 30-day extension; provider admin bottlenecks; authorization errors.', current_workaround='Use ROI vendors; frequent status calls; resubmissions.', why_workaround_fails='Still dependent on provider timelines; error loops reset clocks.', severity='high', frequency='daily', economic_impact='Adds 1–2+ months to cycle time; increases WIP and overhead; risks weaker negotiations due to missing documentation.'), PainPoint(pain='Demand drafting backlog and inconsistent valuation', who_feels_it=['Demand writers', 'Paralegals', 'Attorneys', 'Negotiators'], where_in_workflow='Demand package creation', why_it_persists='Manual chronology/specials; variable writer skill; limited comps; attorney review cycles.', current_workaround='Freelance writers; templates; attorney edits; CaseMetrix in some markets.', why_workaround_fails='Quality variance; slow throughput; limited benchmarks beyond covered geos.', severity='high', frequency='weekly', economic_impact='Weeks added pre-negotiation; potential 5–10% lower opening offers when evidence narrative is weak (inferred).'), PainPoint(pain='Heavy inbound status calls and treatment drop-offs', who_feels_it=['Case managers', 'Paralegals'], where_in_workflow='Treatment tracking', why_it_persists='Anxious clients; few proactive updates; no single channel.', current_workaround='Manual calls; broadcast texts; periodic emails; client apps for some firms.', why_workaround_fails='Low adoption; still high manual work; mixed languages/time windows.', severity='medium', frequency='daily', economic_impact='Staff hours consumed; treatment gaps reduce specials and settlement value.'), PainPoint(pain='Lien resolution and trust disbursement delays post-settlement', who_feels_it=['Lien coordinators', 'Settlement coordinators', 'Accounting/CFO'], where_in_workflow='Settlement/disbursement', why_it_persists='CMS conditional payment/final demand process; multi-payer coordination; strict trust accounting rules.', current_workaround='Third-party lien vendors; manual tracking; monthly reconciliations.', why_workaround_fails='Opaque payer SLAs; documentation ping-pong; reconciliation errors risk sanctions.', severity='high', frequency='weekly', economic_impact='Delays fee recognition and client payment; compliance exposure; additional interest may accrue if Medicare not timely repaid.')] insider_insights=[InsiderInsight(insight='The longest controllable delay before negotiation is not insurer responsiveness but assembling a clean, defensible medical specials package (complete bills, CPT-level itemization, and a credible chronology).', why_non_insiders_miss_it='External observers focus on adjuster delays; PI firms know demands sit idle awaiting corrected bills, provider itemizations, and MMI confirmation.', evidence_type='HIPAA 30+30 day access window; ChartRequest ~30-day average; SmartAdvocate–Compex integration to streamline ROI.'), InsiderInsight(insight='Demand quality drives leverage more than firm brand once at the adjuster’s desk; comps and narrative coherence materially affect opening offers.', why_non_insiders_miss_it='They assume ‘name wins’; adjusters respond to documented damages and locality comps (e.g., CaseMetrix).', evidence_type='TechCrunch on EvenUp demand packages and valuation; CaseMetrix’s positioning as a carrier/plaintiff shared database.'), InsiderInsight(insight='Post-settlement cash conversion is frequently constrained by lien resolution—especially Medicare—rather than accounting; even mature firms wait on CMS final demands before cutting checks.', why_non_insiders_miss_it='They think ‘once it settles, money flows’; Medicare BCRC and final demand rules slow disbursement.', evidence_type='CMS attorney services/conditional payment pages; Synergy Medicare lien FAQs; Florida Bar monthly trust procedures.'), InsiderInsight(insight='Client anxiety is a top hidden cost center; structured mobile updates can halve inbound calls and free case managers to move cases, not just report on them.', why_non_insiders_miss_it='They discount how many hours are lost to status calls in high-volume shops.', evidence_type='Case Status claims of ~50% call reduction; buyer guides citing 30% call and 90% email reductions.')] top_ai_use_cases=[AIUseCase(rank=1, name='AI medical record ingestion → chronology + specials extraction', problem_solved='Manual review of hundreds of pages of records/bills to build a reliable chronology and accurate specials is slow and error-prone, stalling demand readiness.', current_process='Records arrive piecemeal; paralegals read/abstract; enter providers, dates, CPT/ICD, totals into spreadsheets; attorneys spot-check.', workflow_insertion_point='Immediately upon receipt of records/bills; before demand drafting.', buyer='Pre-Litigation Director; COO; Managing Partner', roi_logic='Time savings: 4–8 paralegal hours/case; across 1,000 cases/year → 2–4 FTE freed. Cycle-time: cut pre-demand prep by 1–2 weeks on average (records available to demand writers faster). Quality: fewer missed line items → higher documented specials. Vendors (SmartAdvocate–LawPro.ai; Filevine MedChron-like tools; EvenUp extraction) show feasibility.', proof_metric='Turnaround time from ‘records received’ to ‘chronology/specials approved’; error rate vs human baseline; paralegal hours/case; delta in documented specials per case.', why_existing_software_does_not_fully_solve_it='Core case systems store documents but do not reliably parse unstructured PDFs/EOBs at CPT/charge-level without AI or external tools; manual spreadsheeting persists.'), AIUseCase(rank=2, name='AI-assisted demand package drafting with valuation benchmarks', problem_solved='Demand writing backlogs and uneven quality delay negotiations and depress opening offers.', current_process='Demand writers compile narratives and exhibits manually, referencing limited comps; attorney review cycles add days.', workflow_insertion_point='After records/bills/chronology assembled; before insurer submission.', buyer='Pre-Litigation Director; Managing Partner', roi_logic='Throughput: draft in hours vs days → 1–2 weeks faster to first offer. Capacity: +2–3x demand drafts per writer (vendor claims context). Outcomes: better-structured demands and localized comps improve initial offers (quantify by tracking first-offer % of target over 90 days). Filevine Demands.ai/EvenUp validate adoption path.', proof_metric='Demands per FTE/month; time-to-first-offer; first-offer as % of target value vs pre-AI baseline; attorney redline count per demand.', why_existing_software_does_not_fully_solve_it='Templates exist, but assembling med digests, weaving liability facts, and inserting comps is manual; few systems embed comps and narrative generation end-to-end.'), AIUseCase(rank=3, name='AI-driven intake triage, follow-up, and e-sign orchestration', problem_solved='Missed/slow speed-to-lead and inconsistent qualification reduce signed retainer rates; after-hours leakage.', current_process='Human-only call-backs; manual follow-ups; inconsistent scripts; delayed e-sign dispatch.', workflow_insertion_point='From first contact through retainer signature.', buyer='Intake Director; COO; Managing Partner', roi_logic='Capture: +3–10% relative lift in signed retainers through 24/7 triage, instant scheduling, and automated chase of e-signs (range bounded by vendor claims like Captorra’s +27% capture marketing; adopt conservative subset). Labor: fewer manual touches per lead. Compliance: consistent scripts and conflict checks. CallRail Voice Assist/Lead Docket automations show enabling tech.', proof_metric='Signed retainer rate; speed-to-first-contact; e-sign turnaround; after-hours conversion share; QA scorecards on call transcripts.', why_existing_software_does_not_fully_solve_it='Intake CRMs route leads but do not run autonomous, policy-compliant triage, multilingual callbacks, and persistent e-sign chases after hours without added AI/agents.')] confidence_notes=ConfidenceNotes(high_confidence=['HIPAA 30-day response window with a single 30-day extension shapes ROI cycle time for records (HHS)', 'CMS conditional payment/final demand steps delay disbursement; monthly trust procedures required (CMS; Florida Bar)', 'PI platforms and integrations listed are widely deployed in this ICP (Filevine, Litify, SmartAdvocate, CASEpeer, Neos)', 'Demand automation and comps tools (EvenUp, Filevine Demands.ai, CaseMetrix) are used by PI firms'], inferred_but_not_confirmed=['Per-case time savings for AI chronology (4–8 hours) and demand drafting throughput (2–3x) are inferred from role task analyses and vendor positioning; require firm-specific baselining', 'Economic impact of intake lift (3–10%) depends on lead mix and attorney acceptance criteria'], needs_interviews=['Quantify current demand backlog (cases waiting on drafts) and redline cycles per demand', 'Provider-specific ROI SLAs (by health system) and denial rates driving rework', 'After-hours lead volumes and conversion vs. business hours', 'Lien resolution median days by payer (Medicare vs Medicaid vs ERISA) in this ICP'])

## vertical
Personal Injury (PI) law firms

## icp
- **revenue_range**: $10M–$250M
- **firm_archetypes**: ['High-volume PI settlement firms with centralized intake and pre-litigation teams (multi-state advertising-driven)', 'Boutique PI trial firms with lower intake volume but higher case values and deeper litigation benches', 'Regional PI platforms rolling up solo/small practices onto a common operating stack']
- **buyer_roles**: ['Managing Partner/Owner', 'COO/Director of Operations', 'Intake Director/Marketing Director', 'Pre-Litigation Director', 'Litigation Managing Attorney', 'CFO/Controller (trust/IOLTA oversight)', 'IT/Systems Admin']
- **operating_characteristics**: ['Contingency-fee model; cash conversion dependent on cycle time from incident to disbursement', 'Marketing-heavy funnels (phone/web leads) → centralized intake → pre-lit case building → demand/negotiation → litigation if needed → settlement → lien resolution/disbursement', 'Matter-centric operations with strict deadline tracking (SOL, discovery) and statutory compliance (HIPAA record access windows; Medicare secondary payer rules)', 'Heavy use of PI-specific case management platforms (Filevine, Litify, SmartAdvocate, CASEpeer, Assembly Neos) with integrated intake, e-sign, records retrieval, texting, analytics', 'Staffing by role: intake specialists, case managers, paralegals, demand writers, negotiators (pre-lit adjuster-facing), litigators, lien/settlement coordinators']

## workflow_map
### Item 1
- **stage**: Intake (lead capture)
- **owner_roles**: ['Intake specialists', 'Intake manager', 'Marketing/Call tracking admin']
- **current_process**: Inbound calls/web forms/chat; capture facts (incident date, venue, injuries, at-fault, coverage), conflict check, schedule attorney callback; push to lead/intake system; rapid e-sign of retainer/authorizations if qualified.
- **common_tools**: ['Lead Docket (Filevine)', 'Captorra', 'CallRail (call tracking/AI voice)', 'Kenect (texting)', 'Ngage/chat', 'Vinesign/DocuSign for e-sign']
- **manual_steps**: ['Manual speed-to-lead call-backs and re-attempts', 'Eligibility scripts executed by agents', 'Manual conflict check in DMS/CRM', 'After-hours coverage via answering services']
- **pain_points**: ['Missed/slow response to high-intent calls', 'Inconsistent qualification and documentation', 'After-hours leakage', 'Fragmented comms (phone/text/email)']
- **why_painful**: PI revenue is intake-constrained; lost or delayed contacts convert elsewhere; inconsistent triage admits weak cases and wastes downstream capacity.
- **business_impact**: Lead leakage and variable quality reduce signed retainers; marketing ROI deteriorates; downstream caseload volatility. Captorra markets +27% captured clients through structured intake and follow-up; call tracking/24x7 agents aim to reduce missed calls.
### Item 2
- **stage**: Qualification/Retention
- **owner_roles**: ['Intake specialists', 'Attorneys (screening)']
- **current_process**: Confirm case criteria, venue/SOL window, policy limits where known; obtain signed retainer, HIPAA and records/bills authorizations via e-sign; open matter in case system.
- **common_tools**: ['Lead Docket ↔ Filevine', 'Litify intake', 'Vinesign/DocuSign']
- **manual_steps**: ['Attorney review of borderline cases', 'Chasing signatures by phone/text/email']
- **pain_points**: ['Signature chase delays', 'Borderline-case backlogs']
- **why_painful**: Delay increases client shopping risk; SOL risk for late-filed claims.
- **business_impact**: Lower conversion on qualified leads; escalated attorney time on admin review.
### Item 3
- **stage**: Treatment tracking (pre-lit)
- **owner_roles**: ['Case managers', 'Paralegals']
- **current_process**: Track providers, appointments, and Maximum Medical Improvement (MMI); ensure treatment continuity; log specials (medical bills) and wage loss; client updates via calls/text/app.
- **common_tools**: ['Filevine/CASEpeer/SmartAdvocate treatment modules', 'Case Status (client mobile updates)', 'Kenect texting']
- **manual_steps**: ['Provider scheduling nudges', 'Manual bill tallying in spreadsheets', 'Frequent status calls']
- **pain_points**: ['Treatment gaps and missed appointments', 'High inbound status-call load', 'Manual specials tracking']
- **why_painful**: Gaps devalue cases; staff time diverted to repetitive updates (Case Status claims ~50% fewer inbound calls with app-based updates).
- **business_impact**: Lower settlement value; staff productivity loss; client churn risk.
### Item 4
- **stage**: Medical records and bills acquisition
- **owner_roles**: ['Case managers', 'Records team', 'Paralegals']
- **current_process**: Submit HIPAA-compliant requests to providers; chase status; receive records; organize and upload; request itemized bills and liens.
- **common_tools**: ['ChartRequest/Sharecare/Compex/YoCierge (ROI)', 'SmartAdvocate–Compex integration', 'Filevine docs']
- **manual_steps**: ['Authorization QC; fax/portal submissions; follow-ups; appeal denials; reconcile multiple custodians']
- **pain_points**: ['Cycle time is long and variable; denials for technical errors; volume of follow-ups']
- **why_painful**: HIPAA allows 30 days to respond (one 30-day extension); vendors report ~30-day averages—delays stall demand drafting and negotiation.
- **business_impact**: Adds 30–60+ days to case readiness; increases admin labor; evidence gaps weaken demands.
### Item 5
- **stage**: Demand package creation (pre-suit)
- **owner_roles**: ['Demand writers', 'Paralegals', 'Attorneys (review)']
- **current_process**: Compile liability narrative, med chronology/digests, bills/specials, damages model, photos/police report; draft demand letter and supporting exhibits; quality review; send to carrier.
- **common_tools**: ['EvenUp (AI demand packages)', 'Filevine Demands.ai', 'CaseMetrix (valuation comps)', 'Word/PDF templates']
- **manual_steps**: ['Manual med chronology and damages modeling', 'Iterative edits among writer/attorney', 'Evidence/bill reconciliation']
- **pain_points**: ['Backlog in drafting; inconsistency in valuation and narrative quality; error-prone bill totals']
- **why_painful**: Delays push negotiation start; inconsistent quality depresses offers; attorney review time heavy.
- **business_impact**: Adds weeks; lower opening offers; reduced throughput per FTE.
### Item 6
- **stage**: Negotiation (pre-lit)
- **owner_roles**: ['Negotiators', 'Attorneys', 'Paralegals']
- **current_process**: Submit demand; insurer review; counteroffers; provide supplements; mediate as needed; if impasse, file suit to preserve SOL.
- **common_tools**: ['Email/carrier portals', 'CaseMetrix comps', 'Matter management reminders for SOL']
- **manual_steps**: ['Phone negotiations; compiling supplements; scheduling mediation']
- **pain_points**: ['Slow insurer response; weak comps; SOL pressure']
- **why_painful**: Negotiation windows typically 30–90 days post-demand; poor comps reduce leverage.
- **business_impact**: Prolonged cycle time; higher suit rates when leverage is weak.
### Item 7
- **stage**: Litigation
- **owner_roles**: ['Attorneys', 'Litigation paralegals']
- **current_process**: File and serve; discovery, depositions, expert work; mediation; trial if necessary; many settle post-filing.
- **common_tools**: ['Litify/Filevine/SmartAdvocate for deadlines', 'eDiscovery repositories as needed']
- **manual_steps**: ['Calendar/deadline management', 'Drafting/discovery exchange', 'Scheduling']
- **pain_points**: ['Court-driven delays; discovery burdens; deadline risk']
- **why_painful**: Timelines extend several months to 2+ years depending on venue and complexity.
- **business_impact**: Capital tied up; higher costs; burnout risk.
### Item 8
- **stage**: Settlement, liens, and disbursement
- **owner_roles**: ['Lien coordinators', 'Settlement coordinators', 'CFO/Accounting']
- **current_process**: Confirm settlement terms; identify and resolve liens (Medicare/Medicaid/ERISA/provider); receive funds to trust; calculate fees/costs/client net; generate closing statements; pay liens; disburse client funds; perform trust reconciliations.
- **common_tools**: ['SmartAdvocate disbursements module', 'Synergy/Compass (lien services)', 'Trust accounting (CosmoLex/QuickBooks + trust add-ons)', 'State bar IOLTA resources']
- **manual_steps**: ['Medicare conditional payment disputes; provider negotiations; check cutting; three-way trust reconciliations monthly']
- **pain_points**: ['Lien resolution delays (Medicare final demands post-settlement); reconciliation complexity; uncashed checks follow-up']
- **why_painful**: CMS conditional payment/final demand requirements add weeks; strict trust procedures create admin load; errors are sanction risks.
- **business_impact**: Delays revenue recognition; compliance exposure; client dissatisfaction if disbursement lags.

## technology_map
### Item 1
- **category**: PI case management platforms
- **likely_vendors**: ['Filevine', 'Litify', 'SmartAdvocate', 'CASEpeer', 'Assembly Neos']
- **job_to_be_done**: End-to-end matter, workflow, deadlines, docs, comms, reporting for PI.
- **where_it_breaks**: Customization debt; siloed intake vs demand drafting; record retrieval not native; analytics limited without BI.
- **human_workarounds**: ['Spreadsheets for specials and KPIs', 'Email/phone status updates', 'Manual deadline audits']
### Item 2
- **category**: Intake/lead management & call tracking
- **likely_vendors**: ['Lead Docket (Filevine)', 'Captorra', 'CallRail', 'Ngage live chat']
- **job_to_be_done**: Capture, qualify, route, and sign clients quickly; attribute marketing; reduce missed calls.
- **where_it_breaks**: After-hours responsiveness; inconsistent scripts; fragmented comms channels; limited AI triage.
- **human_workarounds**: ['Answering services', 'Manual call-backs', 'Ad hoc follow-ups via personal phones']
### Item 3
- **category**: Client communication & texting
- **likely_vendors**: ['Case Status', 'Kenect', 'RingCentral texting']
- **job_to_be_done**: Lower inbound status calls; structured updates; reviews capture.
- **where_it_breaks**: Client adoption varies; duplicate channels persist; content not personalized to stage.
- **human_workarounds**: ['Broadcast texts', 'Mass email updates', 'Phone trees']
### Item 4
- **category**: Medical records/bills retrieval (ROI)
- **likely_vendors**: ['ChartRequest', 'Sharecare HDS', 'Compex', 'YoCierge']
- **job_to_be_done**: HIPAA-compliant requests, tracking, and delivery of records/bills.
- **where_it_breaks**: Provider delays; denials for authorizations; multiple custodians; fee disputes.
- **human_workarounds**: ['Fax + phone chases; portal uploads; manual ticklers']
### Item 5
- **category**: Demand drafting and valuation
- **likely_vendors**: ['EvenUp', 'Filevine Demands.ai', 'Internal templates', 'CaseMetrix (comps)']
- **job_to_be_done**: Create persuasive, accurate demand packages; benchmark value; standardize quality.
- **where_it_breaks**: Manual chronology; error-prone specials; uneven narrative; limited comps outside certain regions.
- **human_workarounds**: ['Freelance demand writers', 'Attorney-heavy edits', 'Informal peer comps']
### Item 6
- **category**: Lien resolution & settlement admin
- **likely_vendors**: ['Synergy', 'Compass', 'In-house lien teams']
- **job_to_be_done**: Identify, audit, negotiate, and resolve statutory and provider liens; ensure Medicare compliance; speed disbursement.
- **where_it_breaks**: Opaque payer timelines; manual status checks; document-heavy disputes.
- **human_workarounds**: ['Phone/fax with BCRC/carriers/providers; spreadsheet trackers']
### Item 7
- **category**: Trust/IOLTA accounting & disbursement
- **likely_vendors**: ['CosmoLex', 'TrustBooks', 'QuickBooks + procedures', 'State Bar resources (WSBA, Florida Bar)']
- **job_to_be_done**: Compliant trust accounting, three-way reconciliation, settlement statements, check cutting/ACH.
- **where_it_breaks**: Manual reconciliation and settlement waterfalls; integration gaps with case systems.
- **human_workarounds**: ['Manual three-way monthly reconciliation; journal entries; paper checks']

## pain_point_map
### Item 1
- **pain**: Missed/slow intake follow-up causes lead leakage
- **who_feels_it**: ['Intake specialists', 'Intake manager', 'Managing Partner']
- **where_in_workflow**: Intake
- **why_it_persists**: After-hours coverage gaps; no SLA dashboards; fragmented phone/text/email systems.
- **current_workaround**: Answering services; ad hoc call-backs; manual spreadsheets for follow-ups.
- **why_workaround_fails**: Inconsistent; no attribution/QA; poor client experience.
- **severity**: high
- **frequency**: daily
- **economic_impact**: Each 1% improvement in signed retainer rate on a 5,000-lead/year funnel can add tens of cases and $500k–$1M+ lifetime fee revenue depending on case mix (inferred). Captorra markets +27% capture with structured intake.
### Item 2
- **pain**: 30–60+ day delays to obtain complete medical records and bills
- **who_feels_it**: ['Case managers', 'Paralegals', 'Demand writers']
- **where_in_workflow**: Medical records/bills acquisition
- **why_it_persists**: HIPAA permits 30 days + one 30-day extension; provider admin bottlenecks; authorization errors.
- **current_workaround**: Use ROI vendors; frequent status calls; resubmissions.
- **why_workaround_fails**: Still dependent on provider timelines; error loops reset clocks.
- **severity**: high
- **frequency**: daily
- **economic_impact**: Adds 1–2+ months to cycle time; increases WIP and overhead; risks weaker negotiations due to missing documentation.
### Item 3
- **pain**: Demand drafting backlog and inconsistent valuation
- **who_feels_it**: ['Demand writers', 'Paralegals', 'Attorneys', 'Negotiators']
- **where_in_workflow**: Demand package creation
- **why_it_persists**: Manual chronology/specials; variable writer skill; limited comps; attorney review cycles.
- **current_workaround**: Freelance writers; templates; attorney edits; CaseMetrix in some markets.
- **why_workaround_fails**: Quality variance; slow throughput; limited benchmarks beyond covered geos.
- **severity**: high
- **frequency**: weekly
- **economic_impact**: Weeks added pre-negotiation; potential 5–10% lower opening offers when evidence narrative is weak (inferred).
### Item 4
- **pain**: Heavy inbound status calls and treatment drop-offs
- **who_feels_it**: ['Case managers', 'Paralegals']
- **where_in_workflow**: Treatment tracking
- **why_it_persists**: Anxious clients; few proactive updates; no single channel.
- **current_workaround**: Manual calls; broadcast texts; periodic emails; client apps for some firms.
- **why_workaround_fails**: Low adoption; still high manual work; mixed languages/time windows.
- **severity**: medium
- **frequency**: daily
- **economic_impact**: Staff hours consumed; treatment gaps reduce specials and settlement value.
### Item 5
- **pain**: Lien resolution and trust disbursement delays post-settlement
- **who_feels_it**: ['Lien coordinators', 'Settlement coordinators', 'Accounting/CFO']
- **where_in_workflow**: Settlement/disbursement
- **why_it_persists**: CMS conditional payment/final demand process; multi-payer coordination; strict trust accounting rules.
- **current_workaround**: Third-party lien vendors; manual tracking; monthly reconciliations.
- **why_workaround_fails**: Opaque payer SLAs; documentation ping-pong; reconciliation errors risk sanctions.
- **severity**: high
- **frequency**: weekly
- **economic_impact**: Delays fee recognition and client payment; compliance exposure; additional interest may accrue if Medicare not timely repaid.

## insider_insights
### Item 1
- **insight**: The longest controllable delay before negotiation is not insurer responsiveness but assembling a clean, defensible medical specials package (complete bills, CPT-level itemization, and a credible chronology).
- **why_non_insiders_miss_it**: External observers focus on adjuster delays; PI firms know demands sit idle awaiting corrected bills, provider itemizations, and MMI confirmation.
- **evidence_type**: HIPAA 30+30 day access window; ChartRequest ~30-day average; SmartAdvocate–Compex integration to streamline ROI.
### Item 2
- **insight**: Demand quality drives leverage more than firm brand once at the adjuster’s desk; comps and narrative coherence materially affect opening offers.
- **why_non_insiders_miss_it**: They assume ‘name wins’; adjusters respond to documented damages and locality comps (e.g., CaseMetrix).
- **evidence_type**: TechCrunch on EvenUp demand packages and valuation; CaseMetrix’s positioning as a carrier/plaintiff shared database.
### Item 3
- **insight**: Post-settlement cash conversion is frequently constrained by lien resolution—especially Medicare—rather than accounting; even mature firms wait on CMS final demands before cutting checks.
- **why_non_insiders_miss_it**: They think ‘once it settles, money flows’; Medicare BCRC and final demand rules slow disbursement.
- **evidence_type**: CMS attorney services/conditional payment pages; Synergy Medicare lien FAQs; Florida Bar monthly trust procedures.
### Item 4
- **insight**: Client anxiety is a top hidden cost center; structured mobile updates can halve inbound calls and free case managers to move cases, not just report on them.
- **why_non_insiders_miss_it**: They discount how many hours are lost to status calls in high-volume shops.
- **evidence_type**: Case Status claims of ~50% call reduction; buyer guides citing 30% call and 90% email reductions.

## top_ai_use_cases
### Item 1
- **rank**: 1
- **name**: AI medical record ingestion → chronology + specials extraction
- **problem_solved**: Manual review of hundreds of pages of records/bills to build a reliable chronology and accurate specials is slow and error-prone, stalling demand readiness.
- **current_process**: Records arrive piecemeal; paralegals read/abstract; enter providers, dates, CPT/ICD, totals into spreadsheets; attorneys spot-check.
- **workflow_insertion_point**: Immediately upon receipt of records/bills; before demand drafting.
- **buyer**: Pre-Litigation Director; COO; Managing Partner
- **roi_logic**: Time savings: 4–8 paralegal hours/case; across 1,000 cases/year → 2–4 FTE freed. Cycle-time: cut pre-demand prep by 1–2 weeks on average (records available to demand writers faster). Quality: fewer missed line items → higher documented specials. Vendors (SmartAdvocate–LawPro.ai; Filevine MedChron-like tools; EvenUp extraction) show feasibility.
- **proof_metric**: Turnaround time from ‘records received’ to ‘chronology/specials approved’; error rate vs human baseline; paralegal hours/case; delta in documented specials per case.
- **why_existing_software_does_not_fully_solve_it**: Core case systems store documents but do not reliably parse unstructured PDFs/EOBs at CPT/charge-level without AI or external tools; manual spreadsheeting persists.
### Item 2
- **rank**: 2
- **name**: AI-assisted demand package drafting with valuation benchmarks
- **problem_solved**: Demand writing backlogs and uneven quality delay negotiations and depress opening offers.
- **current_process**: Demand writers compile narratives and exhibits manually, referencing limited comps; attorney review cycles add days.
- **workflow_insertion_point**: After records/bills/chronology assembled; before insurer submission.
- **buyer**: Pre-Litigation Director; Managing Partner
- **roi_logic**: Throughput: draft in hours vs days → 1–2 weeks faster to first offer. Capacity: +2–3x demand drafts per writer (vendor claims context). Outcomes: better-structured demands and localized comps improve initial offers (quantify by tracking first-offer % of target over 90 days). Filevine Demands.ai/EvenUp validate adoption path.
- **proof_metric**: Demands per FTE/month; time-to-first-offer; first-offer as % of target value vs pre-AI baseline; attorney redline count per demand.
- **why_existing_software_does_not_fully_solve_it**: Templates exist, but assembling med digests, weaving liability facts, and inserting comps is manual; few systems embed comps and narrative generation end-to-end.
### Item 3
- **rank**: 3
- **name**: AI-driven intake triage, follow-up, and e-sign orchestration
- **problem_solved**: Missed/slow speed-to-lead and inconsistent qualification reduce signed retainer rates; after-hours leakage.
- **current_process**: Human-only call-backs; manual follow-ups; inconsistent scripts; delayed e-sign dispatch.
- **workflow_insertion_point**: From first contact through retainer signature.
- **buyer**: Intake Director; COO; Managing Partner
- **roi_logic**: Capture: +3–10% relative lift in signed retainers through 24/7 triage, instant scheduling, and automated chase of e-signs (range bounded by vendor claims like Captorra’s +27% capture marketing; adopt conservative subset). Labor: fewer manual touches per lead. Compliance: consistent scripts and conflict checks. CallRail Voice Assist/Lead Docket automations show enabling tech.
- **proof_metric**: Signed retainer rate; speed-to-first-contact; e-sign turnaround; after-hours conversion share; QA scorecards on call transcripts.
- **why_existing_software_does_not_fully_solve_it**: Intake CRMs route leads but do not run autonomous, policy-compliant triage, multilingual callbacks, and persistent e-sign chases after hours without added AI/agents.

## confidence_notes
- **high_confidence**: ['HIPAA 30-day response window with a single 30-day extension shapes ROI cycle time for records (HHS)', 'CMS conditional payment/final demand steps delay disbursement; monthly trust procedures required (CMS; Florida Bar)', 'PI platforms and integrations listed are widely deployed in this ICP (Filevine, Litify, SmartAdvocate, CASEpeer, Neos)', 'Demand automation and comps tools (EvenUp, Filevine Demands.ai, CaseMetrix) are used by PI firms']
- **inferred_but_not_confirmed**: ['Per-case time savings for AI chronology (4–8 hours) and demand drafting throughput (2–3x) are inferred from role task analyses and vendor positioning; require firm-specific baselining', 'Economic impact of intake lift (3–10%) depends on lead mix and attorney acceptance criteria']
- **needs_interviews**: ['Quantify current demand backlog (cases waiting on drafts) and redline cycles per demand', 'Provider-specific ROI SLAs (by health system) and denial rates driving rework', 'After-hours lead volumes and conversion vs. business hours', 'Lien resolution median days by payer (Medicare vs Medicaid vs ERISA) in this ICP']
