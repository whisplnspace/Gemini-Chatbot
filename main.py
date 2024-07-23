import os

import streamlit as st
from streamlit_option_menu import option_menu

from  Gemini_utility import load_gemini_pro_model

working_directory = os.path.dirname(os.path.abspath(__file__))

# setting up the page configuration
st.set_page_config(
    page_title="Gemini AI",
    page_icon="💬",
    layout="centered",
)
with st.sidebar:
    selected = option_menu("Gemini AI",
                       ["ChatBot",
                            "Image Captioning",
                            "Embed text",
                            "Ask Me Anything"],
                           menu_icon = 'robot', icons = ['chat-dots-fill', 'image-fill',
                                                     'textarea-t', 'patch-question-fill'
                                                     ],
                        default_index=0)


    def translate_role_for_streamlit(user_role):
     if user_role == 'model':
        return "assistant"
     else:
        return user_role

if selected != "ChatBot":
    pass
else:
    model = load_gemini_pro_model()
  # Initialize the chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
      st.session_state.chat_session = model.start_chat(history=[])
    # Streamlit_page_title
      st.title("🤖 ChatBot")
  # display the chat history
      for message in st.session_state.chat_session.history:
          with st.chat_message(translate_role_for_streamlit(message.role)):
              st.markdown(message.prts[0].text)

  # input field for user message
      user_prompt = st.chat_input("Ask Gemini Pro..")
      if user_prompt:
       st.chat_message("user").markdown(user_prompt)
      gemini_response = st.session_state.chat_session.send_message(user_prompt)
  # Display Gemini pro response
     with st.chat_message("assistant"):
              st.markdown(gemini_response.text)


