import streamlit as st
import nltk
from nltk.probability import FreqDist

def fetch_nlp_desc(type='df'):
    import spacy
    nlp = spacy.load("en_core_web_lg")
    import pandas as pd
    # read and extract the description from all reviews
    # applies spaCy nlp to each word
    # returns a generator
    df = pd.read_csv(
        './csv/CK_Reviews_Upstart_9-7-2021.csv', usecols=['Review Text'])
    df.dropna(subset=['Review Text'], inplace=True)
    list_text = df['Review Text'].tolist()
    proc_list = [item.lower() for item in list_text]
    if type == 'list':
        text = str(proc_list)
        text = ''.join(text)
        return nlp(text)
    else:
        return nlp.pipe(proc_list, disable=["ner"])


def nounChunk(amount, type, src=fetch_nlp_desc()):
    import pandas as pd
    chunks = []
    for item in src:
        for chunk in item.noun_chunks:
            # for chunk in text.noun_chunks:
            # res = len(chunk.text.split())
            if all(token.is_punct != True for token in chunk) == True:
                if len(chunk) > 1:
                    chunks.append(chunk.text)
    fdist_pos = FreqDist(chunks)
    top_words = fdist_pos.most_common(amount)
    if type == 'list_':
        return top_words
    else:
        return pd.DataFrame(top_words, columns=('Noun Chunk', 'count'))
        # top_words_df.head()


def pos_spaCy():
    df = nounChunk(100, 'df')
    df.to_csv('./csv/nounchunks_Upstart.csv', index=False)
    # st.write(df)


pos_spaCy()
