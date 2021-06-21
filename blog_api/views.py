  
from rest_framework import generics
from rest_framework.serializers import Serializer
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(APIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404



    # def get(self, request, format=None):
    #     transformers = Transformer.objects.all()
    #     serializer = TransformerSerializer(transformers, many=True)
    #     return Response(serializer.data)    
         
    
    # def get_object(self, pk):
    #     # Returns an object instance that should 
    #     # be used for detail views.
    #     try:
    #         return Transformer.objects.get(pk=pk)
    #     except Transformer.DoesNotExist:
    #         raise Http404


    # def put(self, request, pk, format=None):
    #     transformer = self.get_object(pk)
    #     serializer = TransformerSerializer(transformer, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None):
        if id:
            obj_data = get_object_or_404(Post, id=id)
            many = False
        else:
            obj_data = Post.objects.all()
            many = True

        serializer = PostSerializer(obj_data, many=many)

        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id, format=None):
        transformer = self.get_object(id)
        serializer = PostSerializer(transformer,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, id, format=None):
        transformer = self.get_object(id)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      


    



# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer






# from rest_framework import generics
# from blog.models import Post
# from .serializers import PostSerializer

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#     # pass

# class PostDetail(generics.RetrieveDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer