import gradio as gr
from urllib.parse import urlparse, parse_qs
from src.services import get_transcript,user_query_response
from langchain_core.messages import HumanMessage,AIMessage


#Function to get video if from youtube url
def from_url_get_video_id(url_or_id):
    if url_or_id.startswith("http"):
        parsed_url = urlparse(url_or_id)
        video_id = parse_qs(parsed_url.query).get('v', [None])[0]
        return video_id
    return url_or_id


#Funtion for chat history
def format_history(history_list):
    output_string = ""
    for msg in history_list:
        if isinstance(msg,HumanMessage):
            output_string +=f"User: {msg.content}\n"
        elif isinstance(msg,AIMessage):
            output_string +=f"Bot: {msg.content}\n"
    return output_string


def chat_with_llm(video_id,user_query,state):
    current_video_id = state.get("current_video_id")
    ingestion_done = state.get("ingestion_done", False)
    history = state.get("history", [])

    # STOP Condition
    if user_query.lower().strip() in ["stop", "exist", "exists", "quit"]:
        history.append(HumanMessage(content=user_query))
        history.append(AIMessage(content="Thanks for the chat!"))
        state["history"] = history
        new_state = {"current_video_id": None, "ingestion_done": False, "history": history}
        return (
            "Chat ended",
            new_state,
            format_history(history),
            gr.update(value="",interactive=True)
        )

    # If no ingestion done yet → treat as first message
    if not ingestion_done:
        if not video_id:
            return ("Please enter a YouTube URL or ID.", state, format_history(history), gr.update())
        if not user_query or user_query.strip() == "":
            return ("Query cannot be empty!.", state, format_history(history), gr.update())
        
        current_video_id=from_url_get_video_id(video_id)
        # Ingest transcript
        transcript = get_transcript(current_video_id)
        if not transcript:
            history.append(AIMessage(content="Transcript failed to load."))
            return ("Transcript ingestion failed.", state, format_history(history),gr.update())
        
        ingestion_done = True

        # Add the current human message to the internal chat history
        history.append(HumanMessage(content=user_query))

        # Retrieval
        query_response = user_query_response(user_query,current_video_id)
        if query_response["result"] == "No data found":
            final_answer = "The answer is not available in the provided video transcript."
        else:
            final_answer = query_response["result"]


        if len(query_response.get('pages',[]))>0 :
            final_answer += f"\n\nSource pages: {query_response['pages']}"

        # Add the AI's response to the internal chat history
        history.append(AIMessage(content=final_answer))

        # Update state
        new_state = {
            "current_video_id": current_video_id,
            "ingestion_done": True,
            "history": history
        }

        # Return AI response, the updated internal_history_state, and the display_history
        return final_answer,new_state,format_history(history),gr.update(interactive=False)
    
    # Subsequent messages (NO INGESTION)
    if not user_query or user_query.strip() == "":
            return ("Query cannot be empty!.", state, format_history(history), gr.update())
    history.append(HumanMessage(content=user_query))
    query_response = user_query_response(user_query, current_video_id)
    if query_response["result"] == "No data found":
        final_answer = "The answer is not available in the provided video transcript."
    else:
        final_answer = query_response["result"]

    if len(query_response.get("pages", [])) > 0:
        final_answer += f"\nPages: {query_response['pages']}"

    history.append(AIMessage(content=final_answer))

    # Save
    state["history"] = history

    return (
        final_answer,
        state,
        format_history(history),
        gr.update(interactive=False)
    )