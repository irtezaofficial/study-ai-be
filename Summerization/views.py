from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import summarize_url_content

@api_view(['POST'])
def summarize_url(request):
    url = request.data.get('url')
    if not url:
        return Response({'error': 'URL is required'}, status=400)
    
    try:
        summary = summarize_url_content(url)
        return Response({'summary': summary})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
