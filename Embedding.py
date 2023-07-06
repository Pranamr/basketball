import openai
openai.api_key = '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'
response = openai.Embedding(
    model="ada:ft-personal-2023-05-13-12-46-58",
    input="Generate a summary of George Hill performance for the MIL team.")
print(response)