import streamlit as st
import json
from groq_helper import analyze_message, get_areas_of_improvement  # Import AI functions

# Streamlit UI Setup
st.set_page_config(page_title="LoveBot 💖", layout="centered")

# **State Management**
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a flirty, supportive AI assistant that helps couples, listens to their problems, detects complaints, and provides fun relationship advice."}]
if "complaints" not in st.session_state:
    st.session_state.complaints = []  # Stores complaints separately

# **Sidebar Navigation**
page = st.sidebar.radio("📌 Navigate", ["Chat Area", "Your Complaints", "Send Suggestions"])

### **1️⃣ Chat Area Page**
if page == "Chat Area":
    st.markdown("""
        <h1 style="text-align: center; font-size: 2.5em;">
            💖 Flirtify
        </h1>
        <h2 style="text-align: center; font-size: 2em;">
            The one who made Jul<span style="font-weight:bold; color:#FF4B4B;">AI</span>et fall in love with Rom<span style="font-weight:bold; color:#FF4B4B;">AI</span>o 💬
        </h2>
    """, unsafe_allow_html=True)

    st.write("Hey there! I'm here to make your love life fun, drama-free, and full of good vibes. Talk to me! 😉")

    # **Display Chat History**
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # **User Input**
    user_input = st.chat_input("What's on your heart today? ❤️")

    if user_input:
        # Append User Message
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        # **Process Chat & Extract Complaints**
        complaint_text, flirty_response = analyze_message(user_input, st.session_state.messages)

        # **Store Complaint if Found & Avoid Duplicates**
        if complaint_text and complaint_text not in st.session_state.complaints:
            st.session_state.complaints.append(complaint_text)

        # **Display Flirty Response**
        st.session_state.messages.append({"role": "assistant", "content": flirty_response})

        with st.chat_message("assistant"):
            st.markdown(flirty_response)

### **2️⃣ Your Complaints Page**
elif page == "Your Complaints":
    st.markdown("""
        <h1 style="text-align: center; font-size: 2.5em;">
            📜 Your Complaints
        </h1>
    """, unsafe_allow_html=True)

    if st.session_state.complaints:
        st.write("📌 **Here’s what you’ve said about your partner:**")
        for i, complaint in enumerate(st.session_state.complaints, 1):
            st.write(f"🔹 **Complaint {i}:** {complaint}")
    else:
        st.write("You're all good! No complaints stored. 💖")

### **3️⃣ Send Suggestions Page**
elif page == "Send Suggestions":
    st.markdown("""
        <h1 style="text-align: center; font-size: 2.5em;">
            💡 Send Relationship Suggestions
        </h1>
    """, unsafe_allow_html=True)

    if st.button("📩 Send Suggestions"):
        # **Convert Complaints to a Single String**
        complaints_string = " ".join(st.session_state.complaints) if st.session_state.complaints else "No complaints provided."

        # **Call AI Function to Get Relationship Suggestions**
        response = get_areas_of_improvement(complaints_string)

        # **Clear Only Complaints, Keep Messages**
        st.session_state.complaints = []

        # **Display Suggestions**
        st.markdown("""
            <h1 style="text-align: center; font-size: 2.5em;">
                💬 Relationship Improvement Suggestions
            </h1>
        """, unsafe_allow_html=True)

        if "aoi" in response:
            sl_no = 1
            for item in response["aoi"]:
                st.markdown(f"##### {sl_no}) {item['title']}", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:18px;'>{item['suggestion']}</p>", unsafe_allow_html=True)
                sl_no += 1
        else:
            st.write("No suggestions generated.")

        # **Button to Reset & Start Fresh**
        if st.button("🔄 Start Over"):
            st.rerun()
