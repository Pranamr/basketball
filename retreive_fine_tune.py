import os
import openai
openai.api_key = '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'
response = openai.FineTune.retrieve(id="ft-t9Ppyy17VcEcn4PWf5GRqh9y")
print(response)