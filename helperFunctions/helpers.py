from openai import OpenAI
from opensearchpy import OpenSearch
from dotenv import load_dotenv
import os

load_dotenv()

OPENSEARCH_Host = os.getenv("OPENSEARCH_HOST")
OPENSEARCH_PORT = os.getenv("OPENSEARCH_PORT")
OPENSEARCH_USERNAME = os.getenv("OPENSEARCH_USERNAME")
OPENSEARCH_PASSWORD = os.getenv("OPENSEARCH_PASSWORD")
OPENSEARCH_REGION = os.getenv("OPENSEARCH_REGION")
openai_api_key = os.getenv("OPENAI_API_KEY")

def get_OpenAI_client():
  AIClient = OpenAI(
    api_key = openai_api_key,
  )
  return AIClient

def get_OpenSearch_client():
  OSClient = OpenSearch(
    hosts = [{'host': OPENSEARCH_Host, 'port': 443}],
    http_auth = (OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD),
    use_ssl = True,
    verify_certs = True,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
    http_compress=True,
  )
  return OSClient


def get_session_content(session):
  return f'{session["_source"]["content"]} \n timestam: {session["_source"]["timestamp"]}'