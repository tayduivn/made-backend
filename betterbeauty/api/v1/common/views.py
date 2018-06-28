from rest_framework import generics, parsers, permissions

from .serializers import TemporaryImageSerializer


class TemporaryImageUploadView(generics.CreateAPIView):
    parser_classes = [parsers.MultiPartParser, ]
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TemporaryImageSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}
