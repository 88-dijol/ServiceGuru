from rest_framework import serializers

from api.models import Customer,Work


class WorkSerializer(serializers.ModelSerializer):

    customer=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Work

        fields="__all__"

        read_only_fields=["id","customer","created_date","update_date","is_active"]
        

class CustomerSerializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    work_count=serializers.CharField(read_only=True)

    work_total=serializers.CharField(read_only=True)   #nammal aa method kodukumbo oru value kittunolu so namma evide char field kodukanam

    #abov return cheyunnath oru single value aarn so we have given a charfiled but here return cheyunnath not a charfield ,work obj aan return cheyane so for serializing and deserializing there are workserializer so we are giving serializer
    works=WorkSerializer(many=True,read_only=True)   #nested serializer,many=True for 1 customer there will be many works so we are giving this ,so kore obj endavum namuk athine deseri okke cheyanam

    class Meta:

        model=Customer

        fields="__all__"

        read_only_fields=["id","technician","status"," created_date","update_date","is_active"]





