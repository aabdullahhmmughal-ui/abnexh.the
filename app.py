import streamlit as st
from datetime import datetime

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Smart AI Workspace",
    page_icon="🚀",
    layout="wide"
)

# ======================================
# SESSION STATE
# ======================================
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ======================================
# CUSTOM CSS
# ======================================
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
}

.stTextArea textarea {
    background-color: #1e293b;
    color: white;
}

div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
}

.chat-box {
    background-color: #1e293b;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ======================================
# HEADER
# ======================================
st.title("🚀 Smart AI Workspace")
st.subheader("MS Teams + Slack + To-Do + AI Assistant")

# ======================================
# TABS
# ======================================
tab1, tab2, tab3 = st.tabs([
    "💬 Team Chat",
    "✅ To-Do List",
    "🤖 AI Assistant"
])

# ======================================
# TEAM CHAT TAB
# ======================================
with tab1:

    st.header("💬 Team Communication")

    username = st.text_input("Your Name")
    message = st.text_input("Enter Message")

    if st.button("Send Message"):

        if username and message:
            current_time = datetime.now().strftime("%H:%M")

            st.session_state.messages.append(
                f"[{current_time}] {username}: {message}"
            )

    st.subheader("📨 Messages")

    for msg in st.session_state.messages[::-1]:
        st.markdown(
            f"<div class='chat-box'>{msg}</div>",
            unsafe_allow_html=True
        )

# ======================================
# TODO TAB
# ======================================
with tab2:

    st.header("✅ Task Manager")

    new_task = st.text_input("Add New Task")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Add Task"):
            if new_task:
                current_time = datetime.now().strftime("%H:%M")

                st.session_state.tasks.append(
                    f"✅ {new_task} | Added at {current_time}"
                )

    with col2:
        if st.button("Clear Tasks"):
            st.session_state.tasks = []

    st.subheader("📋 Task List")

    for task in st.session_state.tasks[::-1]:
        st.markdown(
            f"<div class='chat-box'>{task}</div>",
            unsafe_allow_html=True
        )

# ======================================
# AI ASSISTANT TAB
# ======================================
with tab3:

    st.header("🤖 AI Assistant")

    user_question = st.text_input(
        "Ask your AI Assistant"
    )

    if st.button("Ask AI"):

        text = user_question.lower()

        # Simple AI Logic
        if "hello" in text:
            response = "Hello 👋 Welcome to Smart AI Workspace!"
        elif "mechanical" in text:
            response = "Mechanical engineering involves machines, design, and thermodynamics ⚙️"
        elif "stress" in text:
            response = "Stress = Force / Area"
        elif "thermodynamics" in text:
            response = "Thermodynamics studies heat and energy 🔥"
        elif "productivity" in text:
            response = "Use the To-Do tab to stay productive ✅"
        else:
            response = f"AI Assistant Response: {user_question}"

        st.session_state.chat_history.append(
            ("You", user_question)
        )

        st.session_state.chat_history.append(
            ("AI", response)
        )

    st.subheader("💡 Conversation")

    for sender, msg in st.session_state.chat_history[::-1]:

        if sender == "You":
            st.markdown(
                f"<div class='chat-box'><b>🧑 You:</b> {msg}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='chat-box'><b>🤖 AI:</b> {msg}</div>",
                unsafe_allow_html=True
            )

# ======================================
# FOOTER
# ======================================
st.markdown("---")
st.markdown(
    "### 🌟 Built by Muhammad Abdullah | Mechanical Engineering Student"
)
