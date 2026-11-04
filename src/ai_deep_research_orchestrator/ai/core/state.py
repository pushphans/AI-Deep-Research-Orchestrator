from typing import Annotated
from typing import TypedDict
from operator import add



class AgentState(TypedDict):
    query : str
    plan : list[str]
    iteration : int
    finding : str
    evaluation : bool
    feedback : str
    findings : Annotated[list[str], add]
    