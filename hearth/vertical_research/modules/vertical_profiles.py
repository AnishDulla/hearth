from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VerticalFocusPack:
    workflow: str = ""
    pains: str = ""
    tech: str = ""
    opportunities: str = ""
    synthesis: str = ""


@dataclass(frozen=True)
class VerticalProfile:
    name: str
    keywords: tuple[str, ...]
    focus: VerticalFocusPack


_PI_LAW_PROFILE = VerticalProfile(
    name="plaintiff_pi_law",
    keywords=("law", "injury", "pi", "plaintiff"),
    focus=VerticalFocusPack(
        workflow=(
            "For plaintiff PI firms, explicitly map intake triage, conflict checks, "
            "retainer conversion, records retrieval, demand drafting, negotiation, and settlement disbursement."
        ),
        pains=(
            "For plaintiff PI firms, include pains in lead qualification, missed follow-ups, "
            "medical-record delays, demand-package throughput, negotiation prep, and lien resolution."
        ),
        tech=(
            "For plaintiff PI firms, inspect CRM/intake tools, case management platforms, "
            "document assembly, e-sign, call tracking, medical-record retrieval services, and analytics tooling."
        ),
        opportunities=(
            "For plaintiff PI firms, prioritize use cases likely to improve signed-case conversion, "
            "time-to-demand, settlement throughput, and staff leverage per case manager/paralegal."
        ),
        synthesis=(
            "PI-law specificity requirements:\n"
            "- Reconstruct intake -> qualification -> retention -> treatment tracking -> medical records -> demand package -> negotiation/litigation -> settlement/disbursement.\n"
            "- Identify roles: intake specialists, case managers, paralegals, attorneys, demand writers, negotiators, lien coordinators.\n"
            "- Quantify where cycle time and case leakage occur."
        ),
    ),
)


VERTICAL_PROFILES: tuple[VerticalProfile, ...] = (
    _PI_LAW_PROFILE,
)


def get_vertical_focus(vertical: str) -> VerticalFocusPack:
    normalized = vertical.lower()
    for profile in VERTICAL_PROFILES:
        if any(keyword in normalized for keyword in profile.keywords):
            return profile.focus
    return VerticalFocusPack()
