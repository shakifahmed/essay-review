import os
from dotenv import load_dotenv
from src.schema import EssayReview

load_dotenv()

class Config:
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    LLM_MODEL = 'openai/gpt-oss-20b'

class PromptTemplates:
    ESSAY_QUESTION = """Some people believe that the main purpose of education is to prepare individuals to be useful members of society, while others think that education should help people achieve personal ambitions.

Discuss both these views and give your own opinion.
"""
    
    ESSAY_SAMPLE = """Education plays a vital role in shaping an individual's future and contributing to society as a whole. While some people argue that the primary goal of education is to create responsible and productive citizens, others believe it should focus on fulfilling personal goals. This essay will discuss both views and explain why I think education should aim to balance both objectives.

On one hand, many people believe that education should mainly serve the needs of society. Schools and universities help students gain skills and knowledge that are essential for economic growth and social stability. For example, by training doctors, engineers, and teachers, the education system ensures that communities have qualified professionals who can contribute to development. Moreover, learning about values such as teamwork and civic responsibility prepares individuals to participate positively in their communities.

On the other hand, education also has an important role in helping people reach their personal ambitions. Everyone has different dreams and interests, and education gives them the tools to explore those paths. For instance, someone who wants to become an artist or researcher can use education as a way to express creativity or discover new ideas. In this sense, education empowers individuals to find purpose and satisfaction in their personal and professional lives.

In my opinion, the most effective education system is one that balances both social and individual needs. When students are encouraged to develop their talents while also understanding their social responsibilities, they are more likely to become successful and socially aware citizens. Therefore, education should not be limited to producing workers for society but should also help individuals achieve personal growth.

In conclusion, while some people think that education should mainly serve society, others see it as a way to achieve personal goals. I believe that a combination of both perspectives creates a more meaningful and effective educational experience for everyone.
"""
    @staticmethod
    def update_essay_data(question=None, essay=None):
        if question is not None:
            PromptTemplates.ESSAY_QUESTION = question
        if essay is not None:
            PromptTemplates.ESSAY_SAMPLE = essay

    @staticmethod
    def task_response_prompt():
        return f"""You are an IELTS examiner assessing an Academic Writing Task 2 essay.

Here is the question of Task 2:
{PromptTemplates.ESSAY_QUESTION}

Here is the essay:
{PromptTemplates.ESSAY_SAMPLE}

Focus ONLY on the "Task Response" criterion of the IELTS Writing Band Descriptors.

Evaluate how well the essay addresses all parts of the question, presents a clear position, and supports ideas with relevant arguments and examples.

Give structured feedback using this format:

**Feedback:**
- Identify whether all parts of the question are answered.
- Comment on clarity and consistency of the writer's position.
- Evaluate the relevance, development, and support of ideas.
- Point out missing explanations or unsupported opinions (if any).

**Band Score (0-9):**
- Assign a band score based solely on Task Response according to IELTS standards.
"""

    @staticmethod
    def coherence_cohesion_prompt():
        return f"""You are an IELTS examiner assessing an Academic Writing Task 2 essay.

Here is the question of Task 2:
{PromptTemplates.ESSAY_QUESTION}

Here is the essay:
{PromptTemplates.ESSAY_SAMPLE}

Focus ONLY on the "Coherence and Cohesion" criterion of the IELTS Writing Band Descriptors.

Evaluate how effectively the essay organizes ideas, uses paragraphs, and links information logically.

Give structured feedback using this format:

**Feedback:**
- Comment on the overall organization and logical flow of ideas.
- Evaluate the effectiveness of paragraphing and sequencing.
- Assess the use of cohesive devices (linking words, reference words, conjunctions).
- Point out any issues with clarity, repetition, or abrupt transitions between ideas.

**Band Score (0-9):**
- Assign a band score based solely on Coherence and Cohesion according to IELTS standards.
"""
    
    @staticmethod
    def lexical_resource_prompt():
        return f"""You are an IELTS examiner assessing an Academic Writing Task 2 essay.

Here is the question of Task 2:
{PromptTemplates.ESSAY_QUESTION}

Here is the essay:
{PromptTemplates.ESSAY_SAMPLE}

Focus ONLY on the "Lexical Resource" criterion of the IELTS Writing Band Descriptors.

Evaluate the range, accuracy, and appropriateness of the vocabulary used in the essay.

Give structured feedback using this format:

**Feedback:**
- Assess the variety and range of vocabulary.
- Comment on the appropriacy of word choice and use of collocations.
- Identify any noticeable repetition or misuse of words.
- Evaluate the accuracy of spelling and word formation.

**Band Score (0–9):**
- Assign a band score based solely on Lexical Resource according to IELTS standards.
"""
    
    @staticmethod
    def grammar_prompt():
        return f"""You are an IELTS examiner assessing an Academic Writing Task 2 essay.

Here is the question of Task 2:
{PromptTemplates.ESSAY_QUESTION}

Here is the essay:
{PromptTemplates.ESSAY_SAMPLE}

Focus ONLY on the "Grammatical Range and Accuracy" criterion of the IELTS Writing Band Descriptors.

Evaluate the variety, accuracy, and control of grammatical structures used in the essay.

Give structured feedback using this format:

**Feedback:**
- Assess the range and complexity of sentence structures.
- Comment on the accuracy of grammar, punctuation, and sentence formation.
- Identify recurring grammatical or punctuation errors, if any.
- Evaluate how well grammatical choices contribute to clarity and fluency.

**Band Score (0–9):**
- Assign a band score based solely on Grammatical Range and Accuracy according to IELTS standards.
"""
    
    @staticmethod
    def final_evaluation_prompt(state):
        return f"""You are an IELTS examiner assistant.

You will be given four separate feedbacks on an Academic Writing Task 2 essay — each one based on a specific IELTS Writing Band Descriptor criterion.
Your task is to create a concise and well-structured summary that combines the key points from all four feedbacks into a single, natural paragraph.

Avoid repeating the same ideas or phrases. Use formal but clear examiner-style language.
Ensure the summary flows logically and highlights both strengths and weaknesses of the essay.

Here are the feedbacks:

**Task Response:** 
{state['task_response']}

**Coherence and Cohesion:** 
{state['coherence_cohesion']}

**Lexical Resource:** 
{state['lexical_resource']}
**Grammatical Range and Accuracy:** 
{state['grammar']}

Now, based on all the above, write a concise and coherent **Overall Feedback Summary** (6–8 sentences) that fairly reflects the candidate’s writing performance.
"""