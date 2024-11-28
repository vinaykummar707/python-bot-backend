from datetime import datetime
from typing import Dict, Any, List, Union
from src.models.prompt_models import PromptResponse

AVAILABLE_DECISIONS: List[str] = ['submit', 'yes', 'no']
DECISION_KEYWORDS: List[str] = ['approve', 'confirm', 'proceed', 'agree', 'accept', 'fill', 'fill up', 'create', 'edit']

def create_response(
    type_: str,
    message: str,
    data: Dict[str, Any] = None,
    needs_decision: bool = False,
    error: str = None,
    details: str = None,
    available_decisions: List[str] = None,
    additional_info: str = None
) -> PromptResponse:
    response_data = {
        "type": type_,
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "requires_decision": needs_decision,
        "data": data or {},
        "error": error,
        "details": details,
        "available_decisions": available_decisions,
        "additional_info": additional_info
    }
    return PromptResponse(**response_data)

def requires_decision(prompt: str) -> bool:
    return any(keyword in prompt.lower().strip() for keyword in DECISION_KEYWORDS)

async def handle_conversation(prompt: str) -> PromptResponse:
    return create_response(
        type_="conversation",
        message="This is a normal conversation response",
        data={"prompt": prompt},
        needs_decision=False
    )

async def handle_decision_request(prompt: str) -> PromptResponse:
    return create_response(
        type_="decision",
        message="This action requires your confirmation",
        data={"prompt": prompt},
        needs_decision=True,
        available_decisions=AVAILABLE_DECISIONS,
        additional_info="Here's the information you need to make a decision"
    )

async def handle_submit(prompt_data: Dict[str, Any]) -> PromptResponse:
    return create_response(
        type_="success",
        message="Data submitted successfully",
        data={"data": prompt_data},
        needs_decision=False
    )

async def handle_yes(prompt_data: Dict[str, Any]) -> PromptResponse:
    return create_response(
        type_="approved",
        message="Request approved",
        data={"data": prompt_data},
        needs_decision=False
    )

async def handle_no(prompt_data: Dict[str, Any]) -> PromptResponse:
    return create_response(
        type_="rejected",
        message="Request rejected",
        data={"data": prompt_data},
        needs_decision=False
    )

async def process_decision(decision: str, prompt_data: Dict[str, Any]) -> PromptResponse:
    decision_handlers = {
        "submit": handle_submit,
        "yes": handle_yes,
        "no": handle_no
    }
    
    handler = decision_handlers.get(decision.lower())
    if not handler:
        raise ValueError(f"Invalid decision: {decision}")
    
    return await handler(prompt_data)

def is_valid_decision(decision: str) -> bool:
    return decision.lower() in [d.lower() for d in AVAILABLE_DECISIONS]
