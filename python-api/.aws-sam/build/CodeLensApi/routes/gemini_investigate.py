# routes/gemini_investigate.py
from fastapi import APIRouter
from pydantic import BaseModel
from services.gemini_services import investigate_code

router = APIRouter() # Connecting to FastAPI main function

class AnalyseIn(BaseModel):
    """
    The request body model.
    Expects a field called 'code' containing the user's Python source.
    """
    code: str


@router.post("/investigate")
def investigate(p: AnalyseIn):
    print("Received code:", p.code)
    """
    Accepts code from the front-end, sends it off to Gemini for analysis,
    and returns the findings – bugs, explanations, and suggested fixes.
    """
    result = investigate_code(p.code)
    return result
