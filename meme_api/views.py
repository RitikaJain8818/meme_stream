from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import MemeModel



@api_view(['GET', 'POST'])
def memes(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets =  MemeModel.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def memeDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = MemeModel.objects.get(pk=pk)
    except MemeModel.DoesNotExist:
        content = {'status_code' : status.HTTP_404_NOT_FOUND, 'detail' : 'Requested object is not available'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        meme_object = MemeModel.objects.get(pk=pk)
        data = request.data
        meme_object.caption = data.get('caption', meme_object.caption)
        meme_object.url = data.get('url', meme_object.url)
        meme_object.save()
        serializer = PostSerializer(meme_object)
        return Response(serializer.data)
