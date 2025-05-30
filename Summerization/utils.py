import re
import requests
from bs4 import BeautifulSoup
from happytransformer import HappyTextToText, TTSettings
from concurrent.futures import ThreadPoolExecutor

summ = HappyTextToText("T5", "google-t5/t5-base")
fast_settings = TTSettings(max_length=150)

def clean_text(text):
    text = re.sub(r'\s*\.\s*', '. ', text.strip())
    text = re.sub(r'\s+', ' ', text)

    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip().capitalize() for s in sentences]
    text = ' '.join(sentences)

    text = re.sub(r'\b(\w+)(, including \1)+', r'\1', text, flags=re.IGNORECASE)

    replacements = {
        'ccommunications': 'communications',
        'teleccommunications': 'telecommunications',
        'alternative definiton': 'alternative definition',
        'point-to-moment': 'point-to-multipoint',
        'ing skew': 'Timing skew',
        'ultipoint': 'multipoint',
        'ommunications': 'communications',
        'ion only': 'Some definitions only',
        'analotransmisssome': 'Analog transmission. Some',
    }
    for wrong, right in replacements.items():
        text = re.sub(wrong, right, text, flags=re.IGNORECASE)

    if not text.endswith('.'):
        text += '.'

    return text

def summarize_chunk(chunk):
    result = summ.generate_text('summarize: ' + chunk, args=fast_settings)

    if hasattr(result, 'text'):
        summary_text = result.text  
    elif isinstance(result, dict):
        summary_text = result.get('summary_text', '')
    else:
        summary_text = str(result)

    return clean_text(summary_text)

def summarize_long_text(text, max_length=512):
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]

    with ThreadPoolExecutor() as executor:
        summaries = list(executor.map(summarize_chunk, chunks))
    print(summaries)
    return summarize_long_texts(' '.join(summaries))

def summarize_url_content(url):
    print("Fetching and scraping the URL content...")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    print("Starting summarization...")
    print(text)
    text = get_relevant_text(text)
    summary = summarize_long_text(text)
    return summary
def get_relevant_text(text):
    words = text.split()
    if len(words) > 5000:
        words = words[:2500]
    return ' '.join(words)
