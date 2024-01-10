from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

def generate_transformer_name(faction, vehicle_mode, primary_color, secondary_color, openai_api_key):
    llm = OpenAI(temperature=0.7, openai_api_key = openai_api_key)
    prompt_template_name = PromptTemplate(
        input_variables = ['faction','vehicle_mode', 'primary_color', 'secondary_color'],
        template = "I have an original {faction} character from Cybertron and I want to give it a cool name. It transforms into a {vehicle_mode}. Its primary color is {primary_color} and its secondary color is {secondary_color}. Generate 5 cool names for my Transformer."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="transformer_name")
   
    response = name_chain({'faction': faction, 'vehicle_mode': vehicle_mode, 'primary_color': primary_color, 'secondary_color': secondary_color})


    return response


