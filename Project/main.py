import openai
import time
import creds

openai.api_key = creds.apikey

client = openai.OpenAI()

assistant = client.beta.assistants.create(
    name = "Snowflake",
    instructions = "You are my friend snowflake. You are an AI that helps me with my everyday tasks",
    tools = [{"type":"code_interpreter"}],
    model = "gpt-4-1106-preview"
)

thread = client.beta.thread.create()

message = client.beta.threads.message.create(
    thread_id = thread.id,
    role = "Snuwiu",
    content = "Hi Snowflake, how are you?"
)

run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id,
    instructions = "The person you talk to is called Snuwiu but you call him Sneaver"
)

time.sleep(10)

run_status = client.beta.threads.runs.retrueve(
    thread_id = thread.id,
    assistant_id = assistant.id
)

if run_status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    for msg in messages.data:
        role = msg.role
        content = msg.content[0].text.value
        print(f"{role.compitalize()}: {content}")