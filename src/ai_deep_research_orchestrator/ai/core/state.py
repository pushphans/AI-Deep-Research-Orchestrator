from typing import Annotated
from typing import TypedDict
from operator import add



class AgentState(TypedDict):
    query : str
    plan : list[str]
    current_step : int
    finding : str
    move_forward : bool
    findings : Annotated[list[str], add]
    