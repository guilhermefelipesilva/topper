import logging
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from rest_framework import generics

logger = logging.getLogger(__name__)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user))

    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer




class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
