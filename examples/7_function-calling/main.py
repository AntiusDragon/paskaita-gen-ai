from rich import print
import os 
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("GITHUB_TOKEN2")
if openai_api_key is None:
    print("Please set GITHUB_TOKEN2 in .env file")

import requests

def get_weather(latitude: str, longitude: str):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    # print(data)
    return data['current']['temperature_2m']

from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=openai_api_key
)

# {"latitude":48.8566,"longitude":2.3522}

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"}
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False
        },
        "strict": True
    }
}]

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

print(completion)

import json
tool_call = completion.choices[0].message.tool_calls[0]
print(tool_call)
args = json.loads(tool_call.function.arguments)

result = get_weather(args["latitude"], args["longitude"])
print(result) 

messages = []

messages.append(completion.choices[0].message)  # append model's function call message
messages.append({                               # append result message
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": str(result)
})

completion_2 = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
)

print(completion_2.choices[0].message.content)