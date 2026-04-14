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
response = client.models.generate_content(model=model_name, contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, temperature=0, tools=[available_functions]))

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

function_results = []

if not response.function_calls:
    print(response.text)
else:
    for function_call in response.function_calls:
        function_call_result = call_function(function_call)

        if not function_call_result.parts:
            raise Exception("Function call returned no parts")

        function_response = function_call_result.parts[0].function_response
        if function_response is None:
            raise Exception("Function response was None")

        if function_response.response is None:
            raise Exception("Function response payload was None")

        function_results.append(function_call_result.parts[0])

        if args.verbose:
            print(f"-> {function_response.response}")
