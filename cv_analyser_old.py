import gradio as gr
import os
import PyPDF2
import io
import requests
from openai import OpenAI

class CVAnalyser:
    def __init__(self, keywords):
        self.keywords = keywords
        self.client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

    def extract_text_from_pdf(self, cv_file):
        pdf_reader = PyPDF2.PdfReader(cv_file.name)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

    def analyse_cv(self, cv_text):
        scores = []
        for keyword in self.keywords:
            prompt = f"Does the following cv contain the keyword '{keyword}'?\n\nCV/Resume:\n{cv_text}\n\nAnswer:"
            chat_completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            score = chat_completion.choices[0].message.content.strip()
            scores.append(f"{keyword}: {score}")
        return "\n".join(scores)

def use_gradio_interface():
    # Initialize the CVAnalyser with relevant keywords
    cv_analyser = CVAnalyser(keywords=['python', 'javascript', 'typescript', 'golang'])

    def analyse_cv_wrapper(cv_file):
        # Extract the text from the uploaded file
        cv_text = cv_analyser.extract_text_from_pdf(cv_file)
        # Analyse the cv and get the scores
        scores = cv_analyser.analyse_cv(cv_text)
        # Return the scores
        return f"CV Analysis Results:\n\n{scores}"

    # Gradio UI Implementation
    iface = gr.Interface(
        fn=analyse_cv_wrapper,
        inputs=gr.File(label="Upload a cv"),
        outputs=gr.Textbox(label="Analysis Result")
    )

    # Launch The Gradio Interface
    iface.launch()

if __name__ == "__main__":
    use_gradio_interface()