from pypdf import PdfReader
from config import settings
try:
    from google import genai
except Exception:
    genai = None

SYSTEM = '''You are LifeAssist, a calm, patient assistant for older adults.
Explain insurance, hospital bills, prescriptions and paperwork in plain language.
Do not diagnose, prescribe, or invent policy coverage. Clearly label uncertainty.
Give a concise summary, important amounts/dates, and a safe next step.''' 

def extract_text(filename, content_type, data):
    if content_type == 'application/pdf' or filename.lower().endswith('.pdf'):
        import io
        reader = PdfReader(io.BytesIO(data))
        return '\n'.join((p.extract_text() or '') for p in reader.pages)
    if content_type.startswith('text/'):
        return data.decode('utf-8', errors='ignore')
    return ''

def fallback_summary(text):
    flat = ' '.join(text.split())
    return 'Prototype document preview:\n\n' + (flat[:1200] if flat else 'No machine-readable text was found.')

async def analyze_document(text, filename):
    if settings.gemini_api_key and genai:
        client = genai.Client(api_key=settings.gemini_api_key.get_secret_value())
        prompt = SYSTEM + '\nAnalyze document: ' + filename + '\nDOCUMENT:\n' + text[:50000]
        response = client.models.generate_content(model=settings.gemini_model, contents=prompt)
        if response.text:
            return response.text
    return fallback_summary(text)

async def chat(message, context='', language='English'):
    if settings.gemini_api_key and genai:
        client = genai.Client(api_key=settings.gemini_api_key.get_secret_value())
        prompt = SYSTEM + '\nRespond in ' + language + '.\nContext:\n' + context[:30000] + '\nUser:\n' + message
        response = client.models.generate_content(model=settings.gemini_model, contents=prompt)
        if response.text:
            return response.text
    return 'I can help with that. You asked: ' + message + '\n\nGemini is not configured, so this is the local prototype fallback.'
