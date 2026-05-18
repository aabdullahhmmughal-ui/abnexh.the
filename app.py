import gradio as gr
from datetime import datetime

# =========================
# Data Storage
# =========================
tasks = []
messages = []

# =========================
# TO-DO FUNCTIONS
# =========================
def add_task(task):
    if task.strip() == "":
        return "\n".join(tasks)

    current_time = datetime.now().strftime("%H:%M")

    tasks.append(f"✅ {task}  |  Added at {current_time}")

    return "\n".join(tasks)


def clear_tasks():
    tasks.clear()
    return ""


# =========================
# TEAM CHAT FUNCTIONS
# =========================
def send_message(name, message):
    if name.strip() == "" or message.strip() == "":
        return "\n".join(messages)

    current_time = datetime.now().strftime("%H:%M")

    messages.append(f"[{current_time}] {name}: {message}")

    return "\n".join(messages)


# =========================
# AI ASSISTANT
# =========================
def ai_assistant(user_message, history):

    text = user_message.lower()

    # Simple AI Logic
    if "hello" in text:
        reply = "Hello 👋 Welcome to your AI Workspace!"
    elif "task" in text:
        reply = "You can manage tasks in the To-Do section ✅"
    elif "meeting" in text:
        reply = "Virtual meetings feature can be added later 🎥"
    elif "mechanical" in text:
        reply = "Mechanical engineering involves machines, thermodynamics, and design ⚙️"
    elif "stress" in text:
        reply = "Stress = Force / Area"
    elif "thermodynamics" in text:
        reply = "Thermodynamics is the study of heat and energy 🔥"
    else:
        reply = f"AI Assistant: I understand your message -> {user_message}"

    history.append((user_message, reply))

    return history


# =========================
# UI DESIGN
# =========================
with gr.Blocks(theme=gr.themes.Soft()) as app:

    gr.Markdown("""
    # 🚀 Smart AI Workspace
    ### MS Teams + Slack + To-Do + AI Assistant
    """)

    with gr.Tabs():

        # =========================
        # TEAM CHAT TAB
        # =========================
        with gr.Tab("💬 Team Chat"):

            gr.Markdown("## Team Communication Channel")

            username = gr.Textbox(
                label="Your Name",
                placeholder="Enter your name"
            )

            message_input = gr.Textbox(
                label="Message",
                placeholder="Type your message..."
            )

            send_btn = gr.Button("Send Message")

            chat_output = gr.Textbox(
                label="Team Messages",
                lines=15
            )

            send_btn.click(
                fn=send_message,
                inputs=[username, message_input],
                outputs=chat_output
            )

        # =========================
        # TO-DO TAB
        # =========================
        with gr.Tab("✅ To-Do List"):

            gr.Markdown("## Manage Your Tasks")

            task_input = gr.Textbox(
                label="New Task",
                placeholder="Enter a task..."
            )

            add_btn = gr.Button("Add Task")

            task_output = gr.Textbox(
                label="Task List",
                lines=12
            )

            clear_btn = gr.Button("Clear Tasks")

            add_btn.click(
                fn=add_task,
                inputs=task_input,
                outputs=task_output
            )

            clear_btn.click(
                fn=clear_tasks,
                outputs=task_output
            )

        # =========================
        # AI ASSISTANT TAB
        # =========================
        with gr.Tab("🤖 AI Assistant"):

            gr.Markdown("## Ask Your AI Assistant")

            chatbot = gr.Chatbot(height=400)

            ai_input = gr.Textbox(
                label="Ask Anything",
                placeholder="Ask engineering or productivity questions..."
            )

            ask_btn = gr.Button("Ask AI")

            ask_btn.click(
                fn=ai_assistant,
                inputs=[ai_input, chatbot],
                outputs=chatbot
            )

    gr.Markdown("""
    ---
    ### 🌟 Features
    - Team Communication
    - Smart To-Do Manager
    - AI Assistant
    - Modern Workspace UI
    """)

# Launch App
app.launch()
