from langchain_ollama import ChatOllama
# from langchain_core.messages import AIMessage

llm = ChatOllama(
    model="deepseek-r1:1.5b",
    temperature=0
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Tamil. Translate the user sentence.",
    ),
    ("human", "I am from Sri Lanka."),
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)