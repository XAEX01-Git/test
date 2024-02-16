import streamlit as st
from chat import get_response, bot_name

BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class StreamlitChatApplication:

    def __init__(self):
        st.set_page_config(page_title="Chat", layout="wide")
        self._init_session_state()

    def _init_session_state(self):
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "enter_pressed" not in st.session_state:
            st.session_state.enter_pressed = False

    def run(self):
        st.title("Chat")
        self._setup_ui()

    def _setup_ui(self):
        st.sidebar.markdown("### Welcome")

        # Display conversation history
        chat_history = st.session_state.chat_history
        if chat_history:
            st.text_area("Conversation:", value="\n".join(chat_history), height=200, max_chars=500)

        # Message entry box
        user_message = st.text_input("Your message:")
        send_button = st.button("Send")

        if send_button or st.session_state.enter_pressed:
            self._on_enter_pressed(user_message)
            st.session_state.enter_pressed = False  # Reset the flag

    def _on_enter_pressed(self, msg):
        if msg:
            user_msg = f"You: {msg}"
            bot_response = f"{bot_name}: {get_response(msg)}"
            self._insert_message(user_msg)
            self._insert_message(bot_response)

    def _insert_message(self, msg):
        st.session_state.chat_history.append(msg)

if __name__ == "__main__":
    app = StreamlitChatApplication()
    app.run()
