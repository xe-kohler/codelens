// src/App.jsx
import GeminiRunner from "./components/GeminiRunner.jsx";
import Header from "./components/Header.jsx";
import InputCodeBlock from "./components/InputCodeBlock.jsx";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8001";

async function checkBackend() { // Health check, Debugging purposes
  try {
    const res = await fetch(`${API_URL}/health`);
    const data = await res.json();
    console.log("✅ Backend connected:", data);
  } catch (err) {
    console.error("❌ Backend not reachable:", err);
  }
}

checkBackend();

let input = `# routes/gemini_investigate.py
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
`;

export default function App() {
  return (
    <main className="min-h-screen top-0 bg-[#181818] text-[#EBEBEB] pt-0 pb-6 flex flex-col items-center min-w-screen">
      <Header/>
      <div className="w-full max-w-full px-20 ">
        <GeminiRunner />
      </div>
    </main>
  );
}
