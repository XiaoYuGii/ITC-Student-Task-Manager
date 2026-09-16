from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer; permission_classes=[permissions.AllowAny]
    def create(self,request,*args,**kwargs):
        r=super().create(request,*args,**kwargs); user=__import__('django.contrib.auth.models',fromlist=['User']).User.objects.get(username=r.data['username']); token,_=Token.objects.get_or_create(user=user); return Response({'token':token.key,'username':user.username},status=201)
class LoginView(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        s=self.serializer_class(data=request.data,context={'request':request}); s.is_valid(raise_exception=True); u=s.validated_data['user']; t,_=Token.objects.get_or_create(user=u); return Response({'token':t.key,'username':u.username})
class TaskListCreate(generics.ListCreateAPIView):
    serializer_class=TaskSerializer
    def get_queryset(self):
        q=Task.objects.filter(owner=self.request.user); status=self.request.query_params.get('status'); return q.filter(status=status) if status else q
    def perform_create(self,s): s.save(owner=self.request.user)
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    def get_queryset(self): return Task.objects.filter(owner=self.request.user)
