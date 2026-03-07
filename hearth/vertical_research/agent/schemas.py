from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class ICPProfile(BaseModel):
    revenue_range: str
    firm_archetypes: list[str] = Field(default_factory=list)
    buyer_roles: list[str] = Field(default_factory=list)
    operating_characteristics: list[str] = Field(default_factory=list)


class WorkflowStage(BaseModel):
    stage: str
    owner_roles: list[str] = Field(default_factory=list)
    current_process: str
    common_tools: list[str] = Field(default_factory=list)
    manual_steps: list[str] = Field(default_factory=list)
    pain_points: list[str] = Field(default_factory=list)
    why_painful: str
    business_impact: str


class TechnologyCategory(BaseModel):
    category: str
    likely_vendors: list[str] = Field(default_factory=list)
    job_to_be_done: str
    where_it_breaks: str
    human_workarounds: list[str] = Field(default_factory=list)


class PainPoint(BaseModel):
    pain: str
    who_feels_it: list[str] = Field(default_factory=list)
    where_in_workflow: str
    why_it_persists: str
    current_workaround: str
    why_workaround_fails: str
    severity: Literal["high", "medium", "low"]
    frequency: Literal["daily", "weekly", "monthly", "quarterly"]
    economic_impact: str


class InsiderInsight(BaseModel):
    insight: str
    why_non_insiders_miss_it: str
    evidence_type: str


class AIUseCase(BaseModel):
    rank: int
    name: str
    problem_solved: str
    current_process: str
    workflow_insertion_point: str
    buyer: str
    roi_logic: str
    proof_metric: str
    why_existing_software_does_not_fully_solve_it: str


class ConfidenceNotes(BaseModel):
    high_confidence: list[str] = Field(default_factory=list)
    inferred_but_not_confirmed: list[str] = Field(default_factory=list)
    needs_interviews: list[str] = Field(default_factory=list)


class VerticalResearchReport(BaseModel):
    vertical: str
    icp: ICPProfile
    workflow_map: list[WorkflowStage] = Field(default_factory=list)
    technology_map: list[TechnologyCategory] = Field(default_factory=list)
    pain_point_map: list[PainPoint] = Field(default_factory=list)
    insider_insights: list[InsiderInsight] = Field(default_factory=list)
    top_ai_use_cases: list[AIUseCase] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes


class WorkflowReport(BaseModel):
    vertical: str
    icp: ICPProfile
    workflow_map: list[WorkflowStage] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes


class PainReport(BaseModel):
    vertical: str
    icp: ICPProfile
    pain_point_map: list[PainPoint] = Field(default_factory=list)
    insider_insights: list[InsiderInsight] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes


class TechReport(BaseModel):
    vertical: str
    icp: ICPProfile
    technology_map: list[TechnologyCategory] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes


class OpportunitiesReport(BaseModel):
    vertical: str
    icp: ICPProfile
    top_ai_use_cases: list[AIUseCase] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes


class AskSynthesis(BaseModel):
    question: str
    answer: str
    evidence_used: list[str] = Field(default_factory=list)
    confidence_notes: ConfidenceNotes
