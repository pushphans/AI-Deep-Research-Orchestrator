from typing import Annotated
from typing import TypedDict
from langchain.messages import AnyMessage
from langgraph.graph.message import add_messages



class AgentState(TypedDict):
    query : str
    plan : list[str]
    current_step : int
    finding : str
    move_to_next_step : bool
    