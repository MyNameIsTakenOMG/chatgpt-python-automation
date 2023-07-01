import requests
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY = os.getenv('OPEN_API_KEY')

parser = argparse.ArgumentParser()
parser.add_argument('prompt', help='prompt to sent to the openai api')
parser.add_argument('file_name', help='name of the file to save python script')
args = parser.parse_args()

api_endpoint = 'https://api.openai.com/v1/completions'
api_key=OPEN_API_KEY

response = requests.post(api_endpoint,headers={
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+ api_key
},json={
    'model': 'text-davinci-003',
    'prompt': f"write python for {args.prompt}",
    'max_tokens': 100,
    'temperature': 0.5
})

if response.status_code == 200:
  # print(response.json()['choices'][0]['text'])
  response_text = response.json()['choices'][0]['text']
  with open(args.file_name,"+w") as file:
    file.write(response_text)
else:
  print(f'Request failed with status code : {str(response.status_code)}')