from helperFunctions.helpers import get_OpenSearch_client
from datetime import datetime
from AIFunctions.embedSession import embedContent


def addSession(request):
  data = request.get_json()

  OSClient = get_OpenSearch_client()

  embedding = embedContent(data["session_content"])
  
  session_document = {
    "content": data["session_content"],
    "user_id": data["user_id"],
    "timestamp": datetime.now().isoformat(),
    "embedding": embedding
  }

  index_name = "sessions"
  response = OSClient.index(index=index_name, body=session_document)
  print(response) 

  return "thanks for the session"



