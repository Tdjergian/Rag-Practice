
from helperFunctions.helpers import get_OpenAI_client




def embedContent(content):

  AIClient = get_OpenAI_client()

  embeddingResponse = AIClient.embeddings.create(
    input = content,
    model = "text-embedding-3-small",
    dimensions = 1536,
    encoding_format = "float",
  )

  return embeddingResponse.data[0].embedding

