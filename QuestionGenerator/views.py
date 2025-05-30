from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import generate_questions

@api_view(['POST'])
def generate_question_api(request):
    text = request.data.get('text')
    if not text:
        return Response({'error': 'Text is required'}, status=400)
    
    try:
        questions = generate_questions(text)
        return Response({'questions': questions})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
