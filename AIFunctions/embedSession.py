from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def embedSession(session_content):

  # Initialize OpenAI client with your API key
  AIClient = OpenAI(
    api_key = openai_api_key,
  )

  embeddingResponse = AIClient.embeddings.create(
    input = session_content,
    model = "text-embedding-3-small",
    dimensions = 1536,
    encoding_format = "float",
  )

  # print("embedding:   ",  embeddingResponse)

  return embeddingResponse.data[0].embedding