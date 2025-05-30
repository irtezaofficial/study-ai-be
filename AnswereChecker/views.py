from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import check_answer_with_context

@api_view(['POST'])
def check_answer_api(request):
    context = request.data.get('Context'),
    question = request.data.get('question')
    user_answer = request.data.get('user_answer')

    if not all([context,question, user_answer]):
        return Response({'error': 'context, question, and user_answer are required.'}, status=400)

    try:
        evaluation = check_answer_with_context(context,question, user_answer)
        return Response({'evaluation': evaluation})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
