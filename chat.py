import streamlit as st


st.set_page_config(page_title="LoveBot 💖", layout="centered")


def display_messages():
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# **State Management**
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a flirty, supportive AI assistant that helps couples, listens to their problems, detects complaints, and provides fun relationship advice."}]
if "complaints" not in st.session_state:
    st.session_state.complaints = []  # Stores complaints separately


# **Sidebar Navigation**
page = st.sidebar.radio("📌 Navigate", ["Chat Area"])

### **1️⃣ Chat Area Page**
if page == "Chat Area":
    # **User Text Input**
    user_input = st.chat_input("What's on your heart today? ❤️ (User typing)", key="user_input")

    if user_input:
        # Append the message from the user
        st.session_state.messages.append({"role": "user", "content": user_input})

        display_messages()

    # **Assistant Text Input**
    assistant_input = st.chat_input("Flirty assistant says... 💌", key="assistant_input")

    if assistant_input:
        # Append the message from the assistant
        st.session_state.messages.append({"role": "assistant", "content": assistant_input})
        display_messages()


