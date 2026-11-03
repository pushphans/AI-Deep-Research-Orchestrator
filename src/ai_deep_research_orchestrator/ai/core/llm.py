from ai_deep_research_orchestrator.core.config import settings
from langchain.chat_models import init_chat_model




llm = init_chat_model(model="gemini-3.1-flash-lite", model_provider="google-genai", api_key = settings.GOOGLE_API_KEY)

