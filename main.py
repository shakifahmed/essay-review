from src.workflow import Workflow
from src.schema import EssayReview
from src.visualization import visual
from config.config import PromptTemplates
import streamlit as st

def main():
#     question = """Some people believe that the main purpose of education is to prepare individuals to be useful members of society, while others think that education should help people achieve personal ambitions.

# Discuss both these views and give your own opinion.
# """
#     essay = """Education is very important for people. Some people think it is for helping society, and some think it is for personal life. I think both are right but education should help people more in their life.

# Firstly, education make people get jobs and work for the country. If people study, they can become doctor or teacher and help others. In this way society become better and people can live good life. Also, if all people are educated, there will be less crime and bad things.

# On the other hand, education is also for person goals. Some people want to be rich or famous, and education help them to do this. For example, if you want to be singer or businessman, you must study. So education can make dreams come true.

# In my opinion, education is very important for everything. People need it for job and for their goals also. So we can say education is for both, society and person.
# """
    question = None
    essay = None
    PromptTemplates.update_essay_data(question, essay)
    
    workflow = Workflow.graph()

    input_data = {'question': question, 'essay': essay}
    
    output = workflow.invoke(input_data)
    
    print("=" * 80)
    print("OVERALL FEEDBACK:")
    print("=" * 80)
    print(output['overall_feedback'])
    print("\n" + "=" * 80)
    print(f"OVERALL BAND SCORE: {output['overall_band']:.1f}")
    print("=" * 80)
    
    print("\nINDIVIDUAL BAND SCORES:")
    print(f"Individual bands: {output['individual_band']}")
    
    try:
        visual(workflow=workflow)
    except Exception as e:
        print(f"\nNote: Workflow visualization failed: {e}")

if __name__ == "__main__":
    main()