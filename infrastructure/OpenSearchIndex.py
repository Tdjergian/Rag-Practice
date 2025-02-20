# from opensearchpy import OpenSearch
# from dotenv import load_dotenv
# import os

# load_dotenv()

# OPENSEARCH_Host = os.getenv("OPENSEARCH_HOST")
# OPENSEARCH_PORT = os.getenv("OPENSEARCH_PORT")
# OPENSEARCH_USERNAME = os.getenv("OPENSEARCH_USERNAME")
# OPENSEARCH_PASSWORD = os.getenv("OPENSEARCH_PASSWORD")
# OPENSEARCH_REGION = os.getenv("OPENSEARCH_REGION")


# client = OpenSearch(
#   hosts = [{'host': OPENSEARCH_Host, 'port': 443}],
#   http_auth = (OPENSEARCH_USERNAME, OPENSEARCH_PASSWORD),
#   use_ssl = True,
#   verify_certs = True,
#   ssl_assert_hostname=False,
#   ssl_show_warn=False,
#   http_compress=True,
# )



# index_name = "sessions"
# index_fields = {
#   "settings": {
#     "number_of_shards": 1,
#     "number_of_replicas": 2, 
#     "index.knn": True,
#   }, 
#   "mappings": {
#     "properties": {
#       "content": {
#         "type": "text"
#       },
#       "user_id": {
#         "type": "keyword"
#       },
#       "timestamp": {
#         "type": "date"
#       },
#       "embedding": {
#         "type": "knn_vector",
#         "dimension": 1536, 
#         "index": True,
#         "similarity": "cosine"
#       }
#     }
#   }
# }
# # mapping = client.indices.get_mapping(index=index_name)
# # print(mapping)
# client.indices.create(index_name, body=index_fields)