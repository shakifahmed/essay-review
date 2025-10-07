from langgraph.graph import StateGraph, START, END
from src.schema import EssayReview
from src.evaluation import EVALUATION

class Workflow:
    @staticmethod
    def graph():
        graph = StateGraph(EssayReview)

        graph.add_node('Evaluate Task Response', EVALUATION.task_response)
        graph.add_node('Evaluate Coherence & Cohesion', EVALUATION.coherence_cohesion)
        graph.add_node('Evaluate Lexical Resource', EVALUATION.lexical_resource)
        graph.add_node('Evaluate Grammar Range', EVALUATION.grammar)
        graph.add_node('Final Evaluation', EVALUATION.final_evaluation)

        graph.add_edge(START, 'Evaluate Task Response')
        graph.add_edge(START, 'Evaluate Coherence & Cohesion')
        graph.add_edge(START, 'Evaluate Lexical Resource')
        graph.add_edge(START, 'Evaluate Grammar Range')

        graph.add_edge('Evaluate Task Response', 'Final Evaluation')
        graph.add_edge('Evaluate Coherence & Cohesion', 'Final Evaluation')
        graph.add_edge('Evaluate Lexical Resource', 'Final Evaluation')
        graph.add_edge('Evaluate Grammar Range', 'Final Evaluation')
        graph.add_edge('Final Evaluation', END)

        workflow = graph.compile()
        return workflow