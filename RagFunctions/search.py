
from helperFunctions.helpers import get_OpenSearch_client
from AIFunctions.embedSession import embedContent

# get session results based on just text
def get_sessions_text(search_text, user_id):

  OSClient = get_OpenSearch_client()

  index_name = "sessions"

  query = {
    "query": {
      "bool":{
        "must": [
          {
            "match": {
              "content": search_text
            }
          },
          {
            "match": {
              "user_id": user_id
            }
          }
        ]
      }
      
    }
  }

  response = OSClient.search(index=index_name, body=query)

  print('hits from text -----------------------------------------------------------')
  hits = response["hits"]["hits"]
  for hit in hits:
    print(hit["_source"]["content"])
    print(hit["_score"])

  return response


# get session results based on just embedding
def get_sessions_embedding(question_embedding, user_id):
  OSClient = get_OpenSearch_client()
  kSize = 10
  index_name = "sessions"

  query = {
    "size": kSize,
    "query": {
        "bool": {
            "must": [
                {
                    "knn": {
                        "embedding": {
                            "vector": question_embedding,
                            "k": kSize
                        }
                    }
                }
            ],
            "filter": [
                {
                    "term": {
                        "user_id": user_id
                    }
                }
            ]
        }
    }
}

  response = OSClient.search(index=index_name, body=query)

  print('hits from embedding -----------------------------------------------------------')
  hits = response["hits"]["hits"]
  for hit in hits:
    print(hit["_source"]["content"])
    print(hit["_score"])

  return response

