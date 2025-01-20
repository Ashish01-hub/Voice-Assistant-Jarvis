from openai import OpenAI 

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# pip install openai
# if you saved the key under a different environment varible name, you can do something like:
client = OpenAI(
 api_key="sk-proj-WxS17ehGk2PnwmzCHcDwT3B1bkFJFMj6bYTk9jG1bqZaFTcj",
)

completion = client.chat.completions.create(
    model="gpt-3-5-turbo",
    message=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choice[0].message.content)  
