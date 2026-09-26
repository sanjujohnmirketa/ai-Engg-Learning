import os
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model=os.environ.get("LLM_MODEL", "claude-sonnet-5"),
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
)
print(response.content[0].text)
