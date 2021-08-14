from django.http.response import Http404
from rest_framework import generics, status,\
   views, permissions, pagination
from rest_framework.response import Response
from blog.models import Article, Comment
from .serializers import AddCommentSerializer, ArticleCreateSerializer,\
  ArticleListSerializer, ArticleDetailsSerializer, CommentSerializer


class StandardResultsSetPagination(pagination.PageNumberPagination):
  page_size = 6
  page_size_query_param = 'page_size'
  max_page_size = 100

# blog list api
class BlogList(generics.ListCreateAPIView):
  queryset = Article.postobjects.all()
  serializer_class = ArticleListSerializer
  pagination_class = StandardResultsSetPagination

# blog detail api
class BlogDetail(generics.RetrieveAPIView):
  serializer_class = ArticleDetailsSerializer

  def get(self, request, slug):
    article = Article.objects.get(slug=slug)
      # .select_related('author__name')\
    serializer = self.serializer_class(article)
    return Response(serializer.data, status=status.HTTP_200_OK)

# blog crud api
class EditBlogApi(views.APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self, pk):
    try:
      return Article.objects.get(pk=pk)
    except Article.DoesNotExist:
      raise Http404

  def add_user_to_data(self, data, user):
    data['author'] = user.id
    return data

  def get(self, request, format=None):
    article = Article.objects.all()
    serializer = ArticleListSerializer(article, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    data = self.add_user_to_data(data=request.data, user=request.user)
    serializer = ArticleCreateSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk, format=None):
    article = self.get_object(pk=pk)
    if article.author == request.user:
      data = self.add_user_to_data(data=request.data, user=request.user)
      serializer = ArticleCreateSerializer(article, data=data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "UnAuthorized"}, status=status.HTTP_403_FORBIDDEN)

  def delete(self, request, pk, format=None):
    article = self.get_object(pk=pk)
    if article.author == request.user:
      article.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "UnAuthorized"}, status=status.HTTP_403_FORBIDDEN)

# comment crud api
class CommentApi(views.APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self, pk):
    try:
      return Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
      raise Http404

  def add_user_to_data(self, data, user):
    data._mutable = True
    data['user'] = user.id
    return data

  def get(self, request, pk, format=None):
    comment = Comment.objects.filter(article__id=pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, format=None):
    data = self.add_user_to_data(data=request.data, user=request.user)
    serializer = AddCommentSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def put(self, request, pk, format=None):
    comment = self.get_object(pk=pk)
    if comment.user == request.user:
      data = self.add_user_to_data(data=request.data, user=request.user)
      serializer = AddCommentSerializer(comment, data=data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "UnAuthorized"}, status=status.HTTP_403_FORBIDDEN)

  def delete(self, request, pk, format=None):
    comment = self.get_object(pk=pk)
    if comment.user == request.user:
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"error": "UnAuthorized"}, status=status.HTTP_403_FORBIDDEN)

