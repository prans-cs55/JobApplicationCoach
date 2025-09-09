# JobApplicationCoach
# 💼 Job Application Coach (Powered by LLMs)

An AI-powered **career assistant** that helps job seekers craft better applications using **Google Gemini** and **Gradio**.  
It combines multiple career-focused tools into one interactive app.

---

## 🚀 Features

- **📄 Cover Letter Generator**  
  Creates tailored cover letters based on the job description and resume content.  

- **📝 Resume Polisher**  
  Improves clarity, relevance, and impact of resumes.  

- **💡 Career Advisor**  
  Suggests resume improvements for better job-role alignment.  

- **🤖 AI Chatbot**  
  Provides instant answers to job and career-related queries.  

---

## ⚙️ Tech Stack

- **Google Gemini API (LLM)** – For text generation  
- **Gradio** – To build the interactive web UI  
- **Google Colab** – Easy deployment and sharing  

---
<img width="2863" height="1550" alt="image" src="https://github.com/user-attachments/assets/7057f9d9-b658-4e10-b73e-82c7a816d8ed" />


job-application-coach/
│── job_application_coach.ipynb # Google Colab Notebook
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-application-coach.git
   cd job-application-coach


Install dependencies:

pip install -r requirements.txt


Open the notebook in Google Colab and add your Gemini API key:

import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")


Run the app:

demo.launch(share=True)
