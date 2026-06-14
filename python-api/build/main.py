import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from mangum import Mangum
from rich.traceback import install

# Load environment variables first
load_dotenv()

# Pretty traceback for debugging
install(show_locals=True)

# --- FastAPI App Setup ---
app = FastAPI(
    title="CodeLens API",
    description="An API that analyses code using Gemini AI and explains bugs or fixes.",
    version="1.0.0",
)

# --- CORS Configuration ---
origins = [
    o.strip()
    for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if o.strip()
]

app.add_middleware(
    CORSMiddleware,
   allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "https://codelens-o2pw.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from routes import gemini_investigate

app.include_router(gemini_investigate.router)

# --- Health Routes ---
@app.get("/")
def root():
    return {"service": "codelens-api", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

# --- AWS Lambda Adapter (optional) ---
lambda_handler = Mangum(app)
