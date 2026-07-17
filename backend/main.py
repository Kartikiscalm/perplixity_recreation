from fastapi import FastAPI, WebSocket
import uvicorn

from services.llm_service import LLMService
from services.sort_source_service import SortSourceService
from services.search_service import SearchService
from pydantic_models.chat_body import ChatBody


app = FastAPI()

search_service = SearchService()
sort_source_service = SortSourceService()
llm_service = LLMService()

#chat-websocket
@app.websocket("/ws/chat")
async def websocket_chat_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        data = await websocket.receive_json()
        print(data)
        query = data.get("query")

        #serch the web and return the sources
        search_results = search_service.web_search(query)
        #sort the sources and get the most relivent ones
        sorted_results = sort_source_service.sort_sources(query, search_results)
        print(sorted_results)
        await websocket.send_json({
            "type":"search_result",
            "data": sorted_results
        })
        print("yooooooo")
        
        #gen the response using llm
        for chunk in llm_service.generate_response(query,sorted_results):
            await websocket.send_json({
                "type": "content",
                "data":chunk
            })
    except Exception:
        print("unexpected error occured")
    finally:
        await websocket.close()

#chat-endpoint 
@app.post("/chat")
def chat_endpoint(body: ChatBody):
    #serch the web and return the sources
    search_results = search_service.web_search(body.query)
    
    #sort the sources and get the most relivent ones
    sorted_results = sort_source_service.sort_sources(body.query, search_results)
    
    #gen the response using llm
    response = "".join(part or "" for part in llm_service.generate_response(body.query,sorted_results))

    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)