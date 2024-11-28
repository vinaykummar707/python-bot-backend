from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, Union
from datetime import datetime

class ErrorResponse(BaseModel):
    error: str
    requires_decision: bool
    details: Optional[str] = None

class PromptRequest(BaseModel):
    prompt: str
    decision: Optional[str] = None
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class PromptResponse(BaseModel):
    type: str
    message: str
    timestamp: str
    requires_decision: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    details: Optional[str] = None
    available_decisions: Optional[list[str]] = None
    additional_info: Optional[str] = None
