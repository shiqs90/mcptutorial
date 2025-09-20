<<<<<<< Updated upstream
=======
import os
>>>>>>> Stashed changes
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
import asyncio
<<<<<<< Updated upstream
import os
=======

>>>>>>> Stashed changes

async def main():
    """_summary_
    """
<<<<<<< Updated upstream
    client = MultiServerMCPClient
    (
=======
    client = MultiServerMCPClient(
>>>>>>> Stashed changes
        
        {
            "calculator":{
                "command":"python",
                 "args":["calculator.py"],
                  "transport":"stdio"
                 
                },
            
            
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
                
            }
            
        }
        
    )
<<<<<<< Updated upstream
    tools = await client.get_tools()
    
    model = ChatGroq(model="qwen-qwq-32b")
=======
    
    tools = await client.get_tools()
    
    model = ChatGroq(model="deepseek-r1-distill-llama-70b")
>>>>>>> Stashed changes
    
    agent = create_react_agent(model, tools)
    
    response = await agent.ainvoke(
<<<<<<< Updated upstream
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    
    print(response[-1].content)

=======
        #{"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
        {"messages": [{"role": "user", "content": "what is a weather in banglore?"}]}
    )
    
    print(response["messages"][-1].content)
>>>>>>> Stashed changes


asyncio.run(main())