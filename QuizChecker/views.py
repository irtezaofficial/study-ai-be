from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .utils import check_answer_with_context
from docx import Document

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def QuizChecker_api(request):
    uploaded_file = request.FILES.get('file')
    context_topic = request.data.get('ContextTopic')

    if not uploaded_file or not context_topic:
        return Response({'error': 'Context topic and .docx file are required.'}, status=400)

    try:
        # Extract text from uploaded .docx file
        doc = Document(uploaded_file)
        extracted_text = "\n".join([para.text for para in doc.paragraphs])

        # Pass to your LLaMA/Ollama answer checker
        reviewed_answer = check_answer_with_context(extracted_text, context_topic)

        return Response({'ReviewedAnswer': reviewed_answer}, status=200)

    except Exception as e:
        return Response({'error': str(e)}, status=500)
