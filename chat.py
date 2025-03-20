import streamlit as st
import streamlit.components.v1 as components

# Initialize chat history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="Chat Interface", layout="wide")

# Apply styles to keep elements fixed and chat scrollable
st.markdown(
    """
    <style>
        .fixed-top {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            z-index: 1000;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .fixed-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: white;
            padding: 10px;
            z-index: 1000;
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.1);
        }
        .chat-container {
            position: fixed;
            top: 70px;
            bottom: 70px;
            left: 0;
            right: 0;
            overflow-y: auto;
            padding: 10px;
        }
        @media screen and (max-width: 768px) {
            .fixed-top, .fixed-bottom {
                padding: 8px;
            }
            .chat-container {
                top: 60px;
                bottom: 60px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Top fixed dropdown
st.markdown("<div class='fixed-top'>", unsafe_allow_html=True)
sender = st.selectbox("Who is texting?", ["Me", "Her"])
st.markdown("</div>", unsafe_allow_html=True)

# Scrollable chat container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    avatar_path = "me_avatar.png" if msg["sender"] == "Me" else "her_avatar.png"
    if msg["sender"] == "Me":
        st.chat_message("user", avatar=avatar_path).write(msg["text"])
    else:
        st.chat_message("assistant", avatar=avatar_path).write(msg["text"])
st.markdown("</div>", unsafe_allow_html=True)

# Bottom fixed input field
st.markdown("<div class='fixed-bottom'>", unsafe_allow_html=True)
message = st.text_input("Type a message:", key="message_input")
if st.button("Send") and message:
    st.session_state.messages.append({"sender": sender, "text": message})
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)
