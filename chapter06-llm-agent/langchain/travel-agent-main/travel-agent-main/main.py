from graph import Graph
import json
import streamlit as st

runnable = Graph()

if __name__ == '__main__':
    # Title of the app
    st.title('Meet your Travel Agent !')

    # Create a text input box
    query = st.text_area('Query:', height = 200)

    # Create a button
    if st.button('Submit'):
        agent_out = runnable.invoke({
        'input' : query,
        'chat_history': []
        })
        
        st.write('Agent :\n\n', json.loads(agent_out['agent_out'])['answer'])

