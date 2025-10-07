from config.config import Config
from langchain_groq import ChatGroq
from src.schema import StructuredReview

class Model:
    @staticmethod
    def get_llm():
        model = ChatGroq(model=Config.LLM_MODEL, api_key=Config.GROQ_API_KEY)
        return model
    
    @staticmethod
    def get_structured_model():
        model = Model.get_llm()
        structured_model = model.with_structured_output(StructuredReview, method="json_schema")
        return structured_model