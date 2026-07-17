from google import genai
from config import Settings 

settings = Settings()

class LLMService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = "gemini-3.1-flash-lite"
    def generate_response(self, query:str, search_results: list[dict]):
        #source 1 -> url then content
        #source 2 -> url then content
        #query
        context_text = "\n\n".join([
            f"Source {i + 1} ({result['url']}):\n{result['content']}"
            for i, result in enumerate(search_results)
        ])

        full_prompt = f"""
        Context from web search:
        {context_text}

        Query: {query}

        provide a comprehensive, detailed, well-cited, accurate response using the above context. 
        think and reason deeply and ensure it answers the qeury that the user is asking.
        do not use the knowledge that you have until absolutely necessary

        """

        response = self.client.models.generate_content_stream(
            model=self.model,
            contents=full_prompt,
        )

        for chunk in response:
            yield chunk.text        
            #yield allows us to come back to the function after going out of the loop, so the function becomes a generator