import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("no API key found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # setting up args

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    client = genai.Client(api_key=api_key)

    for i in range(20):

        if i == 19:
            print("too many function calls at once")
            sys.exit(1)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],system_instruction=system_prompt, temperature=0
            ),
        )

        if response.usage_metadata == None:
            raise RuntimeError("no metadata found, likely api request failed")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate)

        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        function_results = []

        if response.function_calls:
            for f in response.function_calls:
                #print(f"Calling function: {f.name}({f.args})")
                function_call_result = call_function(f, args.verbose)
                if not function_call_result.parts:
                    raise Exception(".parts list empty")
                if not function_call_result.parts[0].function_response:
                    raise Exception("function response is NONE")
                if not  function_call_result.parts[0].function_response.response:
                    raise Exception("function result is NONE")
                function_results.append(function_call_result.parts[0])
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
        else: #nothing left in function calls, print final result and break
            print(response.text)
            break

        messages.append(types.Content(role="user", parts=function_results))

if __name__ == "__main__":
    main()
