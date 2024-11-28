from fastapi import HTTPException
from src.services import prompt_service
from src.models.prompt_models import PromptRequest, PromptResponse, ErrorResponse

async def process_prompt(prompt_request: PromptRequest) -> PromptResponse:
    try:
        if not prompt_request.prompt:
            raise HTTPException(
                status_code=400,
                detail=ErrorResponse(
                    error="Prompt is required",
                    requires_decision=False
                ).dict()
            )

        if not prompt_request.decision:
            if prompt_service.requires_decision(prompt_request.prompt):
                return await prompt_service.handle_decision_request(prompt_request.prompt)
            return await prompt_service.handle_conversation(prompt_request.prompt)

        if not prompt_service.is_valid_decision(prompt_request.decision):
            raise HTTPException(
                status_code=400,
                detail=ErrorResponse(
                    error=f"Invalid decision. Supported decisions are: {', '.join(prompt_service.AVAILABLE_DECISIONS)}",
                    requires_decision=True
                ).dict()
            )

        prompt_data = {
            "prompt": prompt_request.prompt,
            "timestamp": prompt_request.timestamp
        }

        return await prompt_service.process_decision(prompt_request.decision, prompt_data)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                error=str(e),
                requires_decision=True
            ).dict()
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                error="Error processing your request",
                details=str(e),
                requires_decision=False
            ).dict()
        )
