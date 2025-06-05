import getpass
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

response = model.invoke("Hello, Gemini! I'm Laksiri")
print(response.content)