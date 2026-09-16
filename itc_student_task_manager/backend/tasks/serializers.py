from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task
class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=6)
    class Meta: model=User; fields=['username','password','first_name','email']
    def create(self,data): return User.objects.create_user(**data)
class TaskSerializer(serializers.ModelSerializer):
    class Meta: model=Task; fields=['id','title','description','status','priority','due_date','created_at','updated_at']; read_only_fields=['id','created_at','updated_at']
