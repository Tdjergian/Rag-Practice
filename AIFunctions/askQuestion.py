
from helperFunctions.helpers import get_session_content, get_OpenAI_client
from RagFunctions.search import get_sessions_text, get_sessions_embedding
from AIFunctions.embedSession import embedContent

LLM_CONTEXT_PROMPT = '''
You are an assistant for a rock climbing session tracking app that takes relavent notes from past sessions and uses that information to answer questions.
You should be able to answer questions about past sessions and hopefully provide insights into how to help the user continue to stay healthy and keep on training programs.
You should be familiar with Eva Lopez's minimum edge traning protocol, all of Hooper's Beta's content, Eric Horst's training protocols, and any other training protocols that the user mentions they are interested in.
Answer questions only based on the information you have been given in the past sessions, prioritizing information from the most recent sessions.
You do not need to be too long winded in your answers. But make sure to answer questions completely.
You will now recieve a list of recent sessions. Each entry should be considered a separate session.
'''


def askQuestion(request):
  data = request.get_json()

  question = data["question"]
  recent_sessions_prompt = "Here is a list of relevant recent sessions: \n"

  sessions_from_text = get_sessions_text(search_text=question, user_id=data["user_id"])
  sessions_from_text_HITS = sessions_from_text["hits"]["hits"]
  sessions_from_text_content = [get_session_content(session) for session in sessions_from_text_HITS]

  question_embedding = embedContent(question)
  sessions_from_embedding = get_sessions_embedding(question_embedding=question_embedding, user_id=data["user_id"])
  sessions_from_embedding_HITS = sessions_from_embedding["hits"]["hits"]
  sessions_from_embedding_content = [get_session_content(session) for session in sessions_from_embedding_HITS]


  AIClient = get_OpenAI_client()

  response = AIClient.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
      {
        "role": "developer",
        "content": LLM_CONTEXT_PROMPT
      },
      # {
      #   "role": "user",
      #   "content": recent_sessions_prompt + "\n" + "\n".join(sessions_from_text_content)
      # }, 
      {
        "role": "user",
        "content": recent_sessions_prompt + "\n" + "\n".join(sessions_from_embedding_content)
      },
      {
        "role": "user",
        "content": question
      }
    ],
  )
 
  return {
    "response": response.choices[0].message.content,
    "sessions_from_text": sessions_from_text_content,
    "sessions_from_embedding": sessions_from_embedding_content
  }