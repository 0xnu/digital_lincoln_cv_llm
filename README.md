## CV/Resume Analyser

The script analyses CVs/resumes for the presence of specified keywords and extracts the candidate's name and relevant experiences. It uses the OpenAI API to perform the analysis and provides a Gradio interface for user interaction.

### Features

- Extracts text from PDF CVs/resumes
- Analyses CVs/resumes for the presence of specified keywords
- Extracts candidate's name and relevant experiences
- Provides a list of the top three candidates based on the analysis
- Offers a user-friendly Gradio interface for uploading CVs/resumes and viewing the analysis results

### Dependencies

- [OpenAI](https://www.openai.com/)
- [PyPDF2](https://github.com/py-pdf/PyPDF2)
- [Gradio](https://gradio.app/)

### Usage

1. Set the `OPENAI_KEY` environment variable with your OpenAI API key: `export OPENAI_KEY="your_api_key"`
2. Install the required dependencies using `pip install -r requirements.txt`

   ```
    ## Prerequisites
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    python3 -m pip install --upgrade pip
   ```

3. Run the script using `python3 cv_analyser.py`.
4. Access the Gradio interface in your web browser: `http://localhost:7860`
5. Upload the CVs/resumes (maximum 10) in PDF format.
6. Click the "Submit" button to analyse the CVs/resumes.
7. View the analysis results, including the top three candidates' names, relevant keywords, and standout experiences.

### Customisation

- Modify the `keywords` list in the `use_gradio_interface()` function to specify the desired keywords for cv/resume analysis.
- Adjust the prompts in the `analyse_cv()` and `analyse_cvs()` methods to customise the analysis and output format.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

- Thank you, Yas. 🙏🏽 Maybe make it a microservice? 😎 — [Rebel Recruiters](https://www.rebelrecruiters.co.uk/)
- [OpenAI](https://www.openai.com/) for providing the powerful GPT-3.5-turbo language model
- [PyPDF2](https://github.com/py-pdf/PyPDF2) for simplifying the extraction of text from PDF documents
- [Gradio](https://gradio.app/) for enabling the creation of interactive web interfaces

### Copyright

(c) 2024 [Finbarrs Oketunji](https://finbarrs.eu).

Developed at [LincolnHack 2024](https://2024.lincolnhack.org/) in collaboration with [Digital Lincoln](https://www.digitallincoln.co.uk/) — [Lincolnshire](https://en.wikipedia.org/wiki/Lincolnshire) 🇬🇧