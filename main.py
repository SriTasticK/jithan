import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError ("api_key not found")

client = genai.Client(api_key = api_key)
model_name = "gemini-2.5-flash"
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
for each in range(20):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions]
        )
    )

    # Append model response
    if response.candidates:
        candidate = response.candidates[0]
        if candidate.content:
            messages.append(candidate.content)

    if args.verbose:
        print(f"Iteration: {each}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # Final answer
    if not response.function_calls:
        print("Final response:")
        print(response.text)
        break

    function_results = []

    for function_call in response.function_calls:
        if args.verbose:
            print(f"Calling function: {function_call.name}")

        result = call_function(function_call)

        if not result.parts:
            raise Exception("Function call returned no parts")

        part = result.parts[0]

        if part.function_response is None:
            raise Exception("Function response was None")

        if part.function_response.response is None:
            raise Exception("Function response payload was None")

        function_results.append(part)

        if args.verbose:
            print(f"-> {part.function_response.response}")

    # Append tool results (FIXED ROLE)
    messages.append(
        types.Content(role="tool", parts=function_results)
    )

else:
    print("Error: Agent did not complete within 20 iterations.")
    exit(1)
