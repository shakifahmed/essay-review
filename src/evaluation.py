from config.config import PromptTemplates
from src.schema import EssayReview
from src.llm import Model

class EVALUATION:
    @staticmethod
    def task_response(state: EssayReview) -> EssayReview:
        question = state['question']
        essay = state['essay']
        prompt = PromptTemplates.task_response_prompt()
        structured_model = Model.get_structured_model()
        output = structured_model.invoke(prompt)
        return {'task_response': output.feedback, 'individual_band': [output.band]}

    @staticmethod
    def coherence_cohesion(state: EssayReview) -> EssayReview:
        question = state['question']
        essay = state['essay']
        prompt = PromptTemplates.coherence_cohesion_prompt()
        structured_model = Model.get_structured_model()
        output = structured_model.invoke(prompt)
        return {'coherence_cohesion': output.feedback, 'individual_band': [output.band]}
    
    @staticmethod
    def lexical_resource(state: EssayReview) -> EssayReview:
        question = state['question']
        essay = state['essay']
        prompt = PromptTemplates.lexical_resource_prompt()
        structured_model = Model.get_structured_model()
        output = structured_model.invoke(prompt)
        return {'lexical_resource': output.feedback, 'individual_band': [output.band]}
    
    @staticmethod
    def grammar(state: EssayReview) -> EssayReview:
        question = state['question']
        essay = state['essay']
        prompt = PromptTemplates.grammar_prompt()
        structured_model = Model.get_structured_model()
        output = structured_model.invoke(prompt)
        return {'grammar': output.feedback, 'individual_band': [output.band]}
    
    @staticmethod
    def final_evaluation(state: EssayReview) -> EssayReview:
        prompt = PromptTemplates.final_evaluation_prompt(state)
        llm = Model.get_llm()
        output = llm.invoke(prompt)
        overall_feedback = output.content
        overall_band = sum(state['individual_band']) / len(state['individual_band'])
        return {'overall_feedback': overall_feedback, 'overall_band': overall_band}