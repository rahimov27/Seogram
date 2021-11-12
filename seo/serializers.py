from rest_framework import serializers
from .models import *

class BlogListView(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Blog
        fields = '__all__'
