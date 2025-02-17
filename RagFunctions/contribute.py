from flask import Flask, request, jsonify
from opensearchpy import OpenSearch
from dotenv import load_dotenv
from datetime import datetime
from AIFunctions.embedSession import embedSession
import os

load_dotenv()

OPENSEARCH_Host = os.getenv("OPENSEARCH_HOST")
OPENSEARCH_PORT = os.getenv("OPENSEARCH_PORT")
OPENSEARCH_USERNAME = os.getenv("OPENSEARCH_USERNAME")
OPENSEARCH_PASSWORD = os.getenv("OPENSEARCH_PASSWORD")
OPENSEARCH_REGION = os.getenv("OPENSEARCH_REGION")


def addSession(request):
  print('usrename and passwork: ', OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD)
  data = request.get_json()
  print("data.session_content: ", data["session_content"])

  OSClient = OpenSearch(
    hosts = [{'host': OPENSEARCH_Host, 'port': 443}],
    http_auth = (OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD),
    use_ssl = True,
    verify_certs = True,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
    http_compress=True,
  )
  health = OSClient.ping()
  print('health: ', health)

  embedding = embedSession(data["session_content"])
  
  session_document = {
    "session_content": data["session_content"],
    "user_id": data["user_id"],
    "timestamp": datetime.now().isoformat(),
    "embedding": embedding
  }

  index_name = "sessions"
  # OSClient.index(index=index_name, body=session_document)

  return "thanks for the session"



