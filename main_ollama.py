from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("deepseek-r1:1.5b", model_provider="ollama")

response = model.invoke("Hello, deepseek! I'm Laksiri")
print(response.content)
