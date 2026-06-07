# services/gemini_service.py
import os
from google import genai
from google.genai import types


# --- Initialise Gemini client ---
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def investigate_code(code: str) -> dict:
    """
    Ask Gemini to detect bugs, show the corrected code,
    and give a single helpful tip. Output must be short and JSON-structured.
    """

    prompt = f"""
    You are an experienced Python code reviewer. 
    Analyse the following code and respond ONLY in this strict JSON format:
    {{
        "bug_count": <integer>,
        "bugs": [ "brief bug summaries" ],
        "corrected_code": "the corrected Python code, no markdown",
        "tip": "a short single-sentence improvement tip"
    }}

    Rules:
    - Keep it concise (no more than 3 single sentenced bug summaries).
    - No Markdown, no explanations, NO extra commentary.
    - Respond ONLY with valid JSON.

    Code to analyse:
    ```python
    {code}
    ```
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        # Collect text from Gemini’s response
        analysis_text = ""
        for part in response.candidates[0].content.parts:
            if part.text:
                analysis_text += part.text + "\n"

        # Return structured response for frontend
        return {"analysis": analysis_text.strip()}

    except Exception as e:
        # Handle API or network errors gracefully
        return {"error": f"Gemini failed to analyse the code: {str(e)}"}
