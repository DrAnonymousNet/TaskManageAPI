from dataclasses import fields
import imp
from django.forms import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import APIException
from Task.models import Task


class APIException400(APIException):
    status_code = 400

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

 
    def create(self, validated_data):
       state = validated_data.get("state")
       print(state)
       if state != "draft":
           
           raise APIException400("Task State Must Start At Draft")
       return super().create(validated_data)

    def update(self, instance, validated_data):
        previous_state = instance.state
        new_state = validated_data.get("state")

        if previous_state == "draft" and new_state == "done":
            raise APIException400(f"Task Cannot Move From {previous_state} to {new_state}")
        
        if previous_state in ["done", "active"] and new_state == "draft":
            raise APIException400(f"Task Cannot Move From {previous_state} to {new_state}")

       
        if previous_state == "achieved" and new_state != "achieved":
            raise APIException400(f"Task Cannot Move From {previous_state} to {new_state}")
        
        instance.state = new_state
        instance.save()
        return super().update(instance, validated_data)
        
        
        
