from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializer,WorkSerializer

from api.models import Customer

from rest_framework.decorators import action

from rest_framework import status



class CustomerViewSetView(ModelViewSet):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        serializer.save(technician=self.request.user)


# in decorator method creatill use cheyunnath kodukka ,detail ill id pass aakandel True ellel false(here namma customer id kodukkunund so detail =true)
    
    @action(methods=['post'],detail=True)

    def add_work(self,request,*args,**kwargs):

        # customer_instance=self.get_object()

        id=kwargs.get("pk")

        customer_instance=Customer.objects.get(id=id)

        serializer=WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_instance)

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        

