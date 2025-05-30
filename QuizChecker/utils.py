import requests
import base64
import io
from docx import Document

# def extract_text_from_base64_docx(base64_string: str) -> str:
    
#         # Decode base64 string to bytes
#         file_bytes = base64.b64decode(base64_string)
#         print(file_bytes[:4])
#         # Load bytes as a file-like object
#         file_stream = io.BytesIO(file_bytes)

#         # Read DOCX file
#         doc = Document(file_stream)
#         text = '\n'.join([para.text for para in doc.paragraphs])

#         return text



def check_answer_with_context(evaluation,ContextTopic):
    print("answere check karna aa gaya hai")
    prompt = f"""
    You are an expert in {ContextTopic}. Below is a quiz question and an answer. Evaluate if the answer is correct. Respond with "Correct Answere" or "InCorrect Answere" and explain why.
    {evaluation}
    """

    try:
        print(prompt)
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        return f"Error: {str(e)}"
