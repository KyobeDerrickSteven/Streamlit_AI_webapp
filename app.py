import torch
import transformers
from transformers import pipeline, Pipeline
import wikipedia
import streamlit as st

def load_wiki_summary(query: str) -> str:
    results = wikipedia.search(query)
    summary = wikipedia.summary(results[0], sentences=10)
    return summary

def load_qa_pipeline() -> Pipeline:
    qa_pipeline = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')
    return qa_pipeline

def answer_question(pipeline: Pipeline, question: str, paragraph: str) -> dict:
    input = {
        'question': question,
        'context': paragraph
    }
    output = pipeline(input)
    return output

# main app engine
if __name__ == "__main__":
    # The Display of title and description
    st.title('Wikipedia Question Answering')
    st.write('Search topic, ASK questions, Get Answers')
    
    # display of topic input for the user
    topic = st.text_input('Search Topic', "")
    
    # display article paragraph
    article_paragraph = st.empty()
    
    # display question imput slot
    question  =st.text_input("Question", '')
    
    
    if topic:
        # load wikipedia summary of topic
        summary = load_wiki_summary(topic)
        
        # display article summary in paragaraph
        article_paragraph.markdown(summary)
        
        # perform question answering
        if question != "":
            #load question answering pipeline
            qa_pipeline = load_qa_pipeline()
            
            # answer query question using article summary
            result = answer_question(qa_pipeline, question, summary)
            answer = result['answer']
            
            # display answer
            st.write(answer)
            