from rest_framework import viewsets
from .models import Board
from .serializer import BoardSerializer
from rest_framework import mixins
from rest_framework import generics
# from rest_framework.authentication \
#     import BasicAuthentication, SessionAuthentication


class BoardViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        #serializer.save()


class BoardList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BoardDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

