import requests


def check_answer_with_context(context,question, user_answer):
    print("answere check karna aa gaya hai")
    prompt = f"""
You are an examiner evaluating student answers:

Question: {question}

Student's Answer: {user_answer}

Evaluate the student's answer  — do not penalize for grammar, punctuation, or casing.

- If the answer captures the correct meaning, or if it is any where near to being correct then  reply with: "Correct"
- If the meaning is wrong or incomplete, reply with: "Incorrect: <brief reason>"


Keep the response concise.
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
