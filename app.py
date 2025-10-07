import streamlit as st
from src.workflow import Workflow
from config.config import PromptTemplates

st.set_page_config(
    page_title="Essay Review",
    page_icon="📝",
    layout="wide"
)

st.title("Essay Review")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Essay Question")
    question = st.text_area(
        "Enter the essay question:",
        height=150,
        placeholder="Enter the IELTS Writing Task 2 question here...",
        label_visibility="collapsed"
    )

with col2:
    st.subheader("Essay")
    essay = st.text_area(
        "Enter the essay:",
        height=150,
        placeholder="Paste the essay here...",
        label_visibility="collapsed"
    )

st.markdown("---")

if st.button("Review Essay", type="primary", use_container_width=True):
    if not question or not question.strip():
        st.warning("Please enter an essay question.")
    elif not essay or not essay.strip():
        st.warning("Please enter an essay.")
    else:
        with st.spinner("Analyzing your essay... This may take a moment."):
            try:
                PromptTemplates.update_essay_data(question, essay)
                
                workflow = Workflow.graph()
                
                input_data = {'question': question, 'essay': essay}

                output = workflow.invoke(input_data)
                
                st.success("Review Complete!")
                st.markdown("---")
                
                # Display Overall Band Score prominently
                st.subheader("Overall Band Score")
                col_score1, col_score2, col_score3 = st.columns([1, 2, 1])
                with col_score2:
                    st.markdown(f"<h1 style='text-align: center; color: #1f77b4;'>{output['overall_band']:.1f}</h1>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                # Display Individual Band Scores
                st.subheader("Individual Band Scores")
                
                # Create 4 columns for individual scores
                score_col1, score_col2, score_col3, score_col4 = st.columns(4)
                
                # Assuming the order matches: Task Response, Coherence, Lexical, Grammar
                individual_scores = output['individual_band']
                criteria = ["Task Response", "Coherence & Cohesion", "Lexical Resource", "Grammar Range"]
                
                for col, score, criterion in zip([score_col1, score_col2, score_col3, score_col4], individual_scores, criteria):
                    with col:
                        st.metric(label=criterion, value=f"{score:.1f}")
                
                st.markdown("---")
                
                # Display Overall Feedback
                st.subheader("Overall Feedback")
                st.markdown(output['overall_feedback'])
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Please check your API key and configuration.")
else:
    if not question and not essay:
        st.info("Enter an essay question and essay above, then click 'Review Essay' to get feedback.")
    else:
        st.info("Fill in both fields and click 'Review Essay' to get feedback.")