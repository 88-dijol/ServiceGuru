from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import authentication,permissions

from api.serializers import CustomerSerializer,WorkSerializer

from api.models import Customer,Work

from rest_framework.decorators import action

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import status



class CustomerViewSetView(ModelViewSet):

    serializer_class=CustomerSerializer

    queryset=Customer.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def perform_create(self, serializer):

        serializer.save(technician=self.request.user)


#   url: http://127.0.0.1:8000/api/customers/{id}/add_work/

# method:POST
# ee method namma aayit create cheythekunnatha so ethu methodill work cheyunnen nammma paranjukodukanam so dec use aaknam
# in decorator method creatill use cheyunnath kodukka ,detail ill id pass aakandel True ellel false(here namma customer id kodukkunund so detail =true)
    
    @action(methods=['post'],detail=True)

    def add_work(self,request,*args,**kwargs):

        # customer_instance=self.get_object()

        id=kwargs.get("pk")

        customer_instance=Customer.objects.get(id=id)

        serializer=WorkSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(customer=customer_instance)            #customer=customer_instance eth koduthillel integrity error varum   

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        else:

            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


#here create method venda becoz custom aayit namma already customerill add_work enna method create cheythand ,in modelvieswet there is all methods included we dont need all we need to block list,create so we are using this

# from rest_framework.generics.py

#localhost:8000/api/works/{id}/
class WorkMixinView(RetrieveUpdateDestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    queryset=Work.objects.all()

    serializer_class=WorkSerializer


        

