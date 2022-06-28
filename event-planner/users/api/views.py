from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSignupSerializer,PaymentSerializer, VendorSignupSerializer, UserSerializer, UserSerializerForTable
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsCustomerUser, IsManagerUser, IsVendorUser
from ..models import User


@api_view(['GET'])
def view_users(request):
    # checking for the parameters from the URL
    users = User.objects.all()
    serializer = UserSerializerForTable(users, many=True)

    # if there is something in items else raise error
    if users:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class CustomerSignupView(generics.GenericAPIView):
    serializer_class = CustomerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class VendorSignupView(generics.GenericAPIView):
    serializer_class = VendorSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "account created successfully"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'is_customer': user.is_customer,
            'is_vendor': user.is_vendor
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class CustomerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsCustomerUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class VendorOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsVendorUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ManagerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsManagerUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@api_view(['PUT'])
def payments(request, pk):
    user = User.objects.get(pk=pk)
    user.bank_name = request.data.get("bank_name")
    user.bank_number = request.data.get("bank_number")
    user.account_type = request.data.get("account_type")
    serializer = PaymentSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.data)
