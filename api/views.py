from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def home(request):
    product =Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


#@csrf_exempt
@api_view(['POST'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def  createProduct(request):
    product = ProductSerializer(data=request.data)
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return HttpResponse(status=400)


@api_view(['GET'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def readProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product = ProductSerializer(Product)
        return Response(product.data)
    except product.DoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def  deleteProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return HttpResponse(status=204)
    except product.DoesNotExist:
        return HttpResponse(status=404)
