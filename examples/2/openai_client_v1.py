# python week_1/day_2/openai_client/openai_client_v1.py

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

print(api_key)