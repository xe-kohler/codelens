import os
from google import genai
from google.genai import types

# 1. Connect to Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Ask a code question
response = client.models.generate_content(
    model="gemini-2.0-flash",  # change to 2.5 if you have access
    contents="What is the sum of the first 50 prime numbers? "
             "Generate and run code for the calculation.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

# 3. Print the response
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print("TEXT:", part.text)
    if part.executable_code is not None:
        print("CODE:", part.executable_code.code)
    if part.code_execution_result is not None:
        print("RESULT:", part.code_execution_result.output)
