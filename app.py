import os
import argparse

import streamlit as st

from src.cohere import Cohere
from src.openai import OpenAI

st.set_page_config(page_icon="✒️", page_title="Not a Poet")

# parser = argparse.ArgumentParser(description='This app writes poems, but is not a poet.')

# parser.add_argument("--cohere_api_key", help="Add Cohere API key")
# parser.add_argument("--openai_api_key", help="Add OpenAI API key")

# try:
#     args = parser.parse_args()
# except SystemExit as e:
#     # This exception will be raised if --help or invalid command line arguments
#     # are used. Currently streamlit prevents the program from exiting normally
#     # so we have to do a hard exit.
#     os._exit(e.code)
    
# @st.cache_resource()
# def get_llm_connection():
#     """Create a connector using credentials filled in Streamlit secrets"""
#     return Cohere(args.cohere_api_key), OpenAI(api_key=args.openai_api_key)

@st.cache_resource()
def get_llm_connection():
    """Create a connector using credentials filled in Streamlit secrets"""
    return Cohere(st.secrets["COHERE_API_KEY"]), OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


co, oai = get_llm_connection()

st.title("🚫 Not a Poet")

feeling_input = st.text_input("How are you feeling tonight?")

if st.button("Create an abomination"):
    outline_prompt = f"You are a poet laureate and are currently in a room surrounded by other excellent poets. One of them says they feel \"{feeling_input}\". Write an outline of a poem to reflect how this person feels, while impressing the other poets. Outline:"
    outline_res = co.generate(prompt=outline_prompt)
    
    poem_prompt = f"""You are a poet laureate and are currently in a room surrounded by other excellent poets. Here is an outline of a poem. Write a poem using this outline: 

{outline_res}

The poem must be abstract and suitable for a university poetry class. Do not give any into or conclusion. Do not use the outline markers, but format the poem in a traditional way. Only give me a title and poem.

Poem:
"""

    poem_res = co.generate(prompt=poem_prompt)
    
    audio_file = oai.tts(poem_res)
    
    st.audio(data=audio_file)
    
    st.write(poem_res)