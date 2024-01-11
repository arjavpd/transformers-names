import streamlit as st

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

st.title("🤖 Transformers Name Generator")
st.text("This application uses langchain and OpenAI's GPT-3 to generate names for your Transformer.")

faction = st.sidebar.radio("What is your transfomer's faction?", ("Autobot", "Decepticon"))

vehicle_mode = st.sidebar.text_area(
    label="What vehicle does your transformer transform into?",
    max_chars=15
    )

primary_color = st.sidebar.text_area(
    label="What is your Transformer's primary color?",
    max_chars=15
    )

secondary_color = st.sidebar.text_area(
    label="What is your Transformer's secondary color?",
    max_chars=15
    )


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/arjavpd/transformers-names)"

def generate_transformer_name(faction, vehicle_mode, primary_color, secondary_color, openai_api_key):
    llm = OpenAI(temperature=0.7, openai_api_key = openai_api_key)
    prompt_template_name = PromptTemplate(
        input_variables = ['faction','vehicle_mode', 'primary_color', 'secondary_color'],
        template = "I have an original {faction} character from Cybertron and I want to give it a cool name. It transforms into a {vehicle_mode}. Its primary color is {primary_color} and its secondary color is {secondary_color}. Generate 5 cool names for my Transformer."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="transformer_name")
   
    response = name_chain({'faction': faction, 'vehicle_mode': vehicle_mode, 'primary_color': primary_color, 'secondary_color': secondary_color})


    return response


if vehicle_mode:
    if primary_color:
        if secondary_color:
            if not openai_api_key:
                st.info("Please add your OpenAI API key to continue.")
                st.stop()
            response = generate_transformer_name(faction, vehicle_mode, primary_color, secondary_color, openai_api_key)
            st.text(response['transformer_name'])