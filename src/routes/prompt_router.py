from fastapi import APIRouter, HTTPException
from src.controllers import prompt_controller
from src.models.prompt_models import PromptRequest

router = APIRouter()

@router.post("/process-prompt")
async def process_prompt(prompt_request: PromptRequest):
    return await prompt_controller.process_prompt(prompt_request)
