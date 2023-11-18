#streamlit

import streamlit as st
import pandas as pd
import numpy as np
import openai
from openai import OpenAI

from sklearn.metrics.pairwise import cosine_similarity
# from openai.embeddings_utils import get_embeddings, cosine_similarity

st.title("Duke Resources Search Engine")

user_secret = st.text_input(label = ":blue[OpenAI API Key]",
                            placeholder = "Paste your OpenAI API key here",
                            type = "password")

if user_secret:
    openai.api_key = user_secret
    client = OpenAI(api_key=user_secret)

def load_data():
    embedded_groups = pd.read_csv('output/embedded_groups.csv')
    return embedded_groups

def search_notebook(df, search_term, n=3, pprint=True):
    """
    Search for the most similar notes in the dataframe `df` to the search term `search_term`.

    Args:
        df (pd.DataFrame): The dataframe to search.
        search_term (str): The search term.
        n (int): The number of results to return.
        pprint (bool): Whether to print the results.
    
    Returns:
        pd.DataFrame: The top n results.
    """
    
    df['ada_embedding'] = df['ada_embedding'].apply(eval).apply(np.array)

    model = "text-embedding-ada-002"
    search_embedding = client.embeddings.create(input=search_term, model=model).data[0].embedding
    search_embedding = np.array(search_embedding).reshape(1, -1)

    df['similarity'] = df['ada_embedding'].apply(lambda x: cosine_similarity(x.reshape(1,-1), search_embedding))

    result = (
        df.sort_values(by='similarity', ascending=False)
        .head(n)
    )

    if pprint:
        print(result)
    
    return result

search_term = st.text_input(
    label = ":blue[Search]",
    placeholder="Please, search my notebook with..."
)

search_button = st.button(label="Search", type="primary")

if search_term:
    if search_button:
        data = load_data()
        answer = search_notebook(data, search_term, 5, True)

        for index, row in answer.iterrows():
            st.write(row['similarity'][0][0], row['title'], row['link'], row['mission'])