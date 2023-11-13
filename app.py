import streamlit as st
from model import MAX_TEXT_LENGTH, calculate_similarity, MODELS

value_a = """Dear Hanspeter,

I hope this email finds you well. I am writing to propose a meeting to discuss potential collaboration on our upcoming project.

Given your expertise and our shared interest in this area, I believe that combining our efforts could yield significant benefits. I have outlined some preliminary ideas in the attached document, which I hope will serve as a starting point for our discussion.

Would you be available for a meeting on next Thursday at the headquarter? If this does not suit your schedule, please let me know your availability, and I will do my best to accommodate.

Looking forward to the opportunity to work together and exchange ideas.

Best regards,
Marc"""

value_b = """Dear Hanspeter,

Please find attached, the protocol for today's meeting about leveraging AIs capabilities to acquire new customers for your business unit.

Could you please inform your team as well as Martin about the decisions we made? It would be quite a mess if they weren't informed properly.

Greetings,
Marc"""


def calculate_similarity_score():
    st.session_state.similarity_score = calculate_similarity(st.session_state.active_model, st.session_state.text_a,
                                                             st.session_state.text_b)


def model_switched():
    st.toast("Model switched", icon='ℹ')
    calculate_similarity_score()


st.set_page_config(
    page_title="Similarity-Checker",
    page_icon="📚",
    layout="wide",
)

st.title("Similarity Demo")

st.session_state.active_model = st.selectbox("Model", MODELS, index=0, on_change=model_switched)

st.markdown(f"[Model-Information](https://huggingface.co/{st.session_state.active_model})")

col1_texts, col2_texts = st.columns(2)

with col1_texts:
    st.session_state.text_a = st.text_area("Text A", value=value_a, max_chars=MAX_TEXT_LENGTH, height=300)

with col2_texts:
    st.session_state.text_b = st.text_area("Text B", value=value_b, max_chars=MAX_TEXT_LENGTH, height=300)

if st.button("Calculate Similarity"):
    calculate_similarity_score()

if "similarity_score" in st.session_state:
    score = int(st.session_state.similarity_score)
    score_as_string = "Similarity-Score: " + str(score) + "%"
    if score >= 80:
        st.success(score_as_string)
    elif score >= 30:
        st.warning(score_as_string)
    else:
        st.error(score_as_string)