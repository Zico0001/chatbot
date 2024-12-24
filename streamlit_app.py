import streamlit as st

# Example Psychoeducation Modules
psychoeducation_modules = {
    "what_is_trauma": "Trauma is an emotional response to a distressing event. It can result from experiences such as accidents, abuse, or natural disasters. Symptoms can include flashbacks, anxiety, and emotional numbness.",
    "coping_strategies": "Coping strategies include grounding techniques, such as focusing on your senses, deep breathing, journaling, or speaking with a trusted friend or therapist.",
    "self_care": "Self-care involves activities like regular exercise, healthy eating, and ensuring you take time to relax. Remember, seeking help is a sign of strength.",
}

# Example Self-Care Tips
self_care_tips = {
    "stress": "Try deep breathing exercises or progressive muscle relaxation to alleviate stress.",
    "anxiety": "Ground yourself by focusing on your senses: name 5 things you see, 4 things you feel, 3 things you hear, 2 things you smell, and 1 thing you taste.",
    "general": "Engage in regular physical activity, maintain a balanced diet, and set aside time for hobbies and relaxation.",
}

# Streamlit Interface
st.title("Trauma-Informed Chatbot")
st.write("An interactive chatbot for learning about trauma and self-care.")

# User Input
user_input = st.text_input("Enter your question or topic:")
if user_input:
    # Mock response (replace with AI logic if needed)
    response = f"Here's a response related to: {user_input}"
    st.write(response)

# Psychoeducation Modules
st.header("Psychoeducation Modules")
selected_module = st.selectbox(
    "Choose a topic:", list(psychoeducation_modules.keys())
)
if st.button("Get Module Content"):
    st.write(psychoeducation_modules.get(selected_module, "Module not found."))

# Self-Care Tips
st.header("Self-Care Tips")
selected_need = st.selectbox("Select a need:", list(self_care_tips.keys()))
if st.button("Get Self-Care Tip"):
    st.write(self_care_tips.get(selected_need, "No tips available."))

