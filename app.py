import streamlit as st
from model import MAX_TEXT_LENGTH, calculate_similarity

st.title("Similarity Demo")

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

col1, col2 = st.columns(2)

with col1:
    text_a = st.text_area("Text A", value=value_a, max_chars=MAX_TEXT_LENGTH, height=400)

with col2:
    text_b = st.text_area("Text B", value=value_b, max_chars=MAX_TEXT_LENGTH, height=400)

if st.button("Calculate Similarity"):
    similarity = calculate_similarity(text_a, text_b)
    formatted_similarity = "{:.2f}".format(similarity)
    st.markdown(f"Similarity Score: **{formatted_similarity}**")
