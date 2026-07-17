from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

#pydantic will pull the apikey from the .env, using basesettings
class Settings(BaseSettings):
    TAVILY_API_KEY: str = ""
    GEMINI_API_KEY: str = ""