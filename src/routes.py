from .services import get_transcript,user_query_response
from urllib.parse import urlparse, parse_qs



def from_url_get_video_id(url):
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get('v', [None])[0]
    print(video_id)
    return video_id



def lang_chain():
    try:
        video_id = input("Enter the YouTube URL or video ID:").strip()
        if not video_id:
            return "Invalid YouTube URL. No video ID found."
        if video_id.startswith("http"):
            video_id = from_url_get_video_id(video_id)
        transcript = get_transcript(video_id)
        if transcript:
            while True:
                user_query = input("Ask your question (type 'exist' to stop): ").strip().lower()
                if user_query in ["exist", "exists", "stop"]:
                    print("Thanks for the chat!")
                    break
                query_response = user_query_response(user_query,video_id)
                data = {
                    "answer":query_response['result'],
                    "sources":query_response['sources'],
                }
                z=""
                if len(query_response['pages'])>0 :
                    data['pages'] = query_response['pages']
                    z=f"\n\nDerived from the page:{data['pages']}"
                print(f'\nBot response is:{data["answer"]}{z}')
                # return data
        return "Error occurred while ingesting the chunks into Pinecone."
    except Exception as e:
       return str(e)
