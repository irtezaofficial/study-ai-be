from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "voidful/context-only-question-generator")
greedy_settings = TTSettings(no_repeat_ngram_size=2, max_length=1000)

def generate_questions(text, max_length=1024):
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]

    questions = []
    for chunk in chunks:
        result = happy_tt.generate_text(chunk, args=greedy_settings)

        if isinstance(result, dict):
            questions.append(result['text'])
        elif hasattr(result, 'text'):
            questions.append(result.text.strip())
        else:
            raise TypeError("Unknown summary type returned")

    # Convert the joined result into a list of questions
    return [q.strip() for q in '\n'.join(questions).split('\n') if q.strip()]
