import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
@st.cache_resource
def load_model():
    model_name = "EleutherAI/gpt-neo-1.3B"  # Replace with preferred model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# Function to generate responses
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit Interface
st.title("Trauma-Informed Chatbot")
st.write("An interactive chatbot for learning about trauma and self-care, powered by an open-source LLM.")

# User Input
user_input = st.text_input("Ask a question or share your thoughts:")
if user_input:
    with st.spinner("Thinking..."):
        response = generate_response(user_input)
    st.write(response)

# Psychoeducation Modules
st.header("Psychoeducation Modules")
psychoeducation_modules = {
    "what_is_trauma": "Trauma is an emotional response to a distressing event...",
    "coping_strategies": "Coping strategies include grounding techniques...",
    "self_care": "Self-care involves activities like regular exercise and healthy eating...",
}
selected_module = st.selectbox("Choose a topic:", list(psychoeducation_modules.keys()))
if st.button("Get Module Content"):
    st.write(psychoeducation_modules.get(selected_module, "Module not found."))

# Self-Care Tips
st.header("Self-Care Tips")
self_care_tips = {
    "stress": "Try deep breathing exercises to alleviate stress.",
    "anxiety": "Ground yourself by focusing on your senses...",
    "general": "Engage in physical activity and maintain a balanced diet...",
}
selected_need = st.selectbox("Select a need:", list(self_care_tips.keys()))
if st.button("Get Self-Care Tip"):
    st.write(self_care_tips.get(selected_need, "No tips available."))
