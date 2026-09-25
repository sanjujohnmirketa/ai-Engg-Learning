import os

key = os.environ.get('OPENAI_API_KEY');

if key is not None:
    print(f"Environment variable length:' {len(key)}'is set")