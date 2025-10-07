from pydantic import BaseModel, Field
from typing import TypedDict, Annotated
import operator


class StructuredReview(BaseModel):
    feedback: str = Field(description="Analysis of the essay and feedback")
    band: float = Field(description="Score the essay in IELTS Band 0 to 9", ge=0.0, le=9.0)


class EssayReview(TypedDict):
    question: str
    essay: str
    task_response: str
    coherence_cohesion: str
    lexical_resource: str
    grammar: str
    overall_feedback: str
    individual_band: Annotated[list[float], operator.add]
    overall_band: float