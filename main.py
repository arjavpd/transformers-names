import streamlit as st
import langchain_helper as lch

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

if vehicle_mode:
    if primary_color:
        if secondary_color:
            if not openai_api_key:
                st.info("Please add your OpenAI API key to continue.")
                st.stop()
            response = lch.generate_transformer_name(faction, vehicle_mode, primary_color, secondary_color, openai_api_key)
            st.text(response['transformer_name'])