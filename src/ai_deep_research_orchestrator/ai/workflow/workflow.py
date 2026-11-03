from typing import Literal
from ai_deep_research_orchestrator.ai.core.llm import llm
from langchain_core.messages import HumanMessage
from langchain.messages import SystemMessage
from pydantic import Field
from pydantic import BaseModel
from langgraph.graph import START, END, StateGraph
from ai_deep_research_orchestrator.ai.core.state import AgentState


# STRUCTURED OUTPUTS
class PlannerNodeStructuredOutput(BaseModel):
    plan : list[str] = Field(description="steps for researching for user's query")



class EvaluationAgentStructuredOutput(BaseModel):
    eval_result : Literal["Yes", "No"] = Field(description="Evaluation result in Yes or No")



# NODES
async def planner_node(state : AgentState) -> AgentState:

    query = state["query"]

    system_message = SystemMessage(content=f"""
    You are a planner agent. 
    You will take user's query and will generate steps to be taken to respond to user's query accurately.
    Steps will be saved in order in a list
    """)


    human_message = HumanMessage(content=f"""
    Here is the user's query : \n{query}
    """)


    planner_llm = llm.with_structured_output(PlannerNodeStructuredOutput)

    response : PlannerNodeStructuredOutput = await planner_llm.ainvoke([system_message, human_message])

    return {
        "plan" : response.plan
    }



async def researcher_node(state : AgentState) -> AgentState:
    plan = state["plan"]
    current_step = state["current_step"]

    executable_step = plan[current_step]

    system_message = SystemMessage(content=f"""
    You are the researcher agent.
    You will be getting topics to research.
    Make sure to do proper research and create a summarised version of your research.
    """)

    human_message = HumanMessage(content=f"""
    Topic for the research : \n{executable_step}
    """)

    response = await llm.ainvoke([system_message, human_message])

    return {
        "finding" : response.content
    }



async def evaluation_node(state : AgentState) -> AgentState:
    query = state["query"]
    finding = state["finding"]

    move_to_next_step = state["move_to_next_step"]

    system_message = SystemMessage(content=f"""
    You are the evaluator agent. 
    You have user's original query.
    You also have researcher agent's finding.
    You have to check if the researcher agent's findings are suitable for the query or not.
    No highest accuracy is needed just check if its relevant or not. 
    If the finding is relevant reply with "Yes" and if its not then reply with "No"
    """)


    human_message = HumanMessage(content=f"""
    This is the original query of user : {query}
    This is the researcher agent's finding : {finding}
    """)


    eval_llm = llm.with_structured_output(EvaluationAgentStructuredOutput)

    response : EvaluationAgentStructuredOutput = await eval_llm.ainvoke([system_message, human_message])

    return 





