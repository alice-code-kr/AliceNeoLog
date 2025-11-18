from asyncio import tools
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage
from langchain_core.messages import ChatMessage
from langchain.tools import tool
from datetime import datetime
from langchain.messages import AIMessage
from langchain.messages import ToolMessage


@tool
def get_now() -> str:
   """이거는 한국 현재시간을 알려주는 함수야. 한국 현재 시간을 물어보면 이 함수를 실행해."""
   now = datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S.%f초")
   return now
class NeoChatBot():
   def __init__(self):
      self.llm = ChatOllama(
         model="gpt-oss:latest",
         temperature=0,
         validate_model_on_init=True,
         base_url="http://192.168.219.109:11434"
      ).bind_tools([get_now])

   def ask(self,message):
      messages = [
         ChatMessage(role="system", content="넌 내 말에 친한 친구처럼 대답해줘.그리고 한국어로 대답해줘."),
         HumanMessage(message)
      ]
      ai_msg = self.llm.invoke(messages)
      print(ai_msg)
      if isinstance(ai_msg, AIMessage) and ai_msg.tool_calls:
         for k in ai_msg.tool_calls:
            if k["name"] == 'get_now': 
               tool = ToolMessage( 
                 content=get_now.invoke({}),
                 tool_call_id= k["id"] 
               )
               messages.append(tool)
               print(self.llm.invoke(messages))

         

            print(ai_msg.tool_calls)
         
   





