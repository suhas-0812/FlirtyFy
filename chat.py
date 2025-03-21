import streamlit as st


st.set_page_config(page_title="LoveBot 💖", layout="centered")


def display_messages():
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            with st.chat_message("me", avatar="me.jpeg"):
                st.markdown(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("her", avatar="her.jpg"):
                st.markdown(msg["content"])

def spectrum_progress_bar(value: int):
    """
    Responsive progress bar that smoothly transitions from red to green based on value (0–100),
    using viewport height (vh) for dynamic sizing.
    """
    if not (0 <= value <= 100):
        st.error("Value must be between 0 and 100.")
        return

    # Convert score to color using HSL
    hue = int((value / 100) * 120)

    st.markdown(f"""
        <div style="position: relative; height: 2.2vh; background-color: #eee; border-radius: 1vh; overflow: hidden;">
            <div style="
                width: {value}%;
                height: 100%;
                background-color: hsl({hue}, 100%, 50%);
                transition: width 0.4s ease;
            "></div>
            <div style="
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                line-height: 2.2vh;
                font-weight: 500;
                font-size: 1.3vh;
                color: #000;
            ">
                {value}%
            </div>
        </div>
    """, unsafe_allow_html=True)





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
    user_input = st.chat_input("Your message", key="user_input")

    if user_input:
        # Append the message from the user
        st.session_state.messages.append({"role": "user", "content": user_input})

        display_messages()
        spectrum_progress_bar(2)

    # **Assistant Text Input**
    assistant_input = st.chat_input("Her message", key="assistant_input")

    if assistant_input:
        # Append the message from the assistant
        st.session_state.messages.append({"role": "assistant", "content": assistant_input})
        display_messages()

