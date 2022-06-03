from .models import Toppings, Person, Songs, Movies, FoodItems, Books
from .serializers import ToppingSerializer, PersonSerializer, SongsSerializer, MovieSerializer, FoodItemsSerializer, BookSeializer
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

#Class Based View Implementation

#Easy Class Based View





#ListAPIView
class ToppingListView(ListAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer


class ToppingCreateView(CreateAPIView):
   queryset = Toppings.objects.all()
   serializer_class = ToppingSerializer


class ToppingUpdateView(UpdateAPIView):
     queryset = Toppings.objects.all()
     serializer_class = ToppingSerializer

class ToppingsRetrieveView(RetrieveAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

class ToppingsDeleteView(DestroyAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer


# Mixins Implementation - 31-05-2022
class ToppingsList(GenericAPIView, ListModelMixin):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ToppingsCreate(GenericAPIView, CreateModelMixin):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ToppingsUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

    def post(self,request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ToppingsRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

    def get(self, request,pk, *args, **kwargs):
        return self.retrieve(request *args, **kwargs)

class ToppingsDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer

    def destroy(self, request, pk, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)

#Viewsets Implementation

class ToppingsViewSet(viewsets.ViewSet):
    def list(self,request):
        t = Toppings.objects.all()
        serializer = ToppingSerializer(t,many=True)
        return Response(serializer.data)

    def create(self,request):
        t = Toppings.objects.all()
        serializer = ToppingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        id = pk
        if id is not None:
            t = Toppings.objects.get(id = id)
            serializer = ToppingSerializer(t)
            return Response(serializer.data)

    def update(self,request,pk=None):
        id = pk
        if id is not None:
            t = Toppings.objects.get(pk = id)
            serializer = ToppingSerializer(t, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Updated'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        id = pk
        if id is not None:
            t = Toppings.objects.get(pk = id)
            t.delete()
            return Response({'msg':'Record Deleted'})

#ModelViewsets

class ToppingsModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer


#Read Only Model Viewsets

class ReadOnlyToppings(viewsets.ReadOnlyModelViewSet):
    queryset = Toppings.objects.all()
    serializer_class = ToppingSerializer


class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class SongDemo(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class ModelMovies(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class ModelFood(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = FoodItems.objects.all()
    serializer_class = FoodItemsSerializer

class ModelBook(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Books.objects.all()
    serializer_class = BookSeializer