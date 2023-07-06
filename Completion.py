import openai
openai.api_key = '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'
response = openai.Completion.create(
    model="ada:ft-personal-2023-05-13-12-46-58",
    prompt="Generate a summary of George Hill performance for the MIL team.",
    max_tokens=150)
print(response)

#ada:ft-personal-2023-05-13-09-25-37
#ada:ft-personal-2023-05-13-10-55-28"
#ada:ft-personal-2023-05-13-11-17-29
#ada:ft-personal-2023-05-12-07-47-27
#ada:ft-personal-2023-05-13-12-46-58