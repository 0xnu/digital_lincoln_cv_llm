import gradio as gr
import os
import PyPDF2
import io
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
        prompt = f"Analyse the following cv for the presence of keywords {', '.join(self.keywords)}. Also, extract the candidate's name and relevant experiences.\n\nCV/Resume:\n{cv_text}\n\nAnalysis:"
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        analysis = chat_completion.choices[0].message.content.strip()
        return analysis

    def analyse_cvs(self, cv_files):
        analyses = []
        for cv_file in cv_files:
            cv_text = self.extract_text_from_pdf(cv_file)
            analysis = self.analyse_cv(cv_text)
            analyses.append(analysis)
        prompt = f"Given the following cv analyses:\n\n{'-'*40}\n{'-'*40}\n".join(analyses) + "\n\nProvide a list of the top three candidates, including their names, relevant keywords, and experiences that make them stand out. Format the output as a numbered list."
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        top_candidates = chat_completion.choices[0].message.content.strip()
        return top_candidates

def use_gradio_interface():
    def analyse_cvs_wrapper(cv_files, keywords):
        # If cv_files is not a list, convert it to a list
        if not isinstance(cv_files, list):
            cv_files = [cv_files]
        
        # Initialize the CVAnalyser with the provided keywords
        cv_analyser = CVAnalyser(keywords=keywords.split(','))
        top_candidates = cv_analyser.analyse_cvs(cv_files)
        return top_candidates

    # Gradio UI Implementation
    iface = gr.Interface(
        fn=analyse_cvs_wrapper,
        inputs=[
            gr.File(label="Upload CVs (Maximum 10)", file_count="multiple"),
            gr.Textbox(label="Enter Keywords (comma-separated)")
        ],
        outputs=gr.Textbox(label="Analysis Result")
    )

    # Launch The Gradio Interface
    iface.launch()

if __name__ == "__main__":
    use_gradio_interface()