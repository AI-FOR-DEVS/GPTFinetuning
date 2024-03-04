from openai import OpenAI

# Create the client

client = OpenAI()

# Upload the training file

response = client.files.create(
    file=open('data.jsonl', 'rb'),
    purpose='fine-tune'
)

print(response)

# Create the fine-tuned model

client.fine_tuning.jobs.create(
    training_file=response.id,
    model="gpt-3.5-turbo"
)

# Use the fine-tuned model

completion = client.chat.completions.create(
    model="Your Model ID", 
    messages=[
        {
            "role": "system", "content": "You are the AI mentor, Sebastian. You offer guidance, share experiences, and answer questions."
        },
        {
            "role": "user", "content": "What can I expect learning in the CrewAI Course?"
        }
    ]
)

print(completion.choices[0].message)