# Install required packages
!pip install -q google-generativeai gradio

import google.generativeai as genai
import gradio as gr

# 🔑 Configure Gemini API
genai.configure(api_key="YOUR_API_KEY")

# Select model
model = genai.GenerativeModel("gemini-1.5-flash")

# ---- Functions ----
def cover_letter_app(company_name, position_name, job_description, resume_content):
    prompt = f"""
    Generate a customized cover letter for:
    - Company: {company_name}
    - Position: {position_name}
    - Job Description: {job_description}
    - Resume: {resume_content}

    Use only experiences from my resume. Highlight alignment with job requirements.
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=512, temperature=0.7)
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def resume_polisher_app(position_name, resume_content, polish_prompt=""):
    if polish_prompt.strip():
        prompt = f"Polish this resume for a {position_name} role: {resume_content}. Instructions: {polish_prompt}"
    else:
        prompt = f"Polish this resume for a {position_name} role: {resume_content}. Improve clarity, relevance, and impact."

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=512, temperature=0.7)
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def chatbot_app(user_input):
    try:
        response = model.generate_content(
            user_input,
            generation_config=genai.types.GenerationConfig(max_output_tokens=256, temperature=0.7)
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def career_advisor_app(position_applied, job_description, resume_content):
    prompt = f"""
    Considering job: {position_applied}
    Job Description: {job_description}
    Resume: {resume_content}

    Suggest improvements to align the resume better with the job requirements.
    """
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(max_output_tokens=512, temperature=0.7)
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ---- Gradio Interfaces ----
cover_letter_interface = gr.Interface(
    fn=cover_letter_app,
    inputs=[gr.Textbox(label="Company Name"),
            gr.Textbox(label="Position Name"),
            gr.Textbox(label="Job Description"),
            gr.Textbox(label="Resume Content")],
    outputs=gr.Textbox(label="Generated Cover Letter"),
    title="Cover Letter Generator"
)

resume_polisher_interface = gr.Interface(
    fn=resume_polisher_app,
    inputs=[gr.Textbox(label="Position Name"),
            gr.Textbox(label="Resume Content"),
            gr.Textbox(label="Optional Instructions")],
    outputs=gr.Textbox(label="Polished Resume"),
    title="Resume Polisher"
)

chatbot_interface = gr.Interface(
    fn=chatbot_app,
    inputs=gr.Textbox(label="Ask something"),
    outputs=gr.Textbox(label="Response"),
    title="AI Chatbot"
)

career_advisor_interface = gr.Interface(
    fn=career_advisor_app,
    inputs=[gr.Textbox(label="Position Applied"),
            gr.Textbox(label="Job Description"),
            gr.Textbox(label="Resume Content")],
    outputs=gr.Textbox(label="Career Advice"),
    title="Career Advisor"
)

# ---- Tabbed App ----
app = gr.TabbedInterface(
    [cover_letter_interface, resume_polisher_interface, chatbot_interface, career_advisor_interface],
    tab_names=["Cover Letter", "Resume Polisher", "Chatbot", "Career Advisor"]
)

# 🚀 Launch in Colab with share=True
app.launch(share=True, debug=True)
