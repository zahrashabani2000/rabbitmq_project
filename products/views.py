from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, User
from .serializers import ProductSerializser
from .producer import publish

import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializser = ProductSerializser(products, many=True)
        return Response(serializser.data)

    def create(self,request):
        serializer = ProductSerializser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Products.objects.get(id=pk)
        serializser = ProductSerializser(product)
        return Response(serializser.data)
    
    def update(self, resquest, pk=None):
        product = Products.objects.get(id=pk)
        serializer = ProductSerializser(instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None):
        product = Products.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserApiView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
