from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Review
        fields = ['title', 'video_link', 'img', 'text', 'published', 'comment', 'owner' ] # 'owner'


class UserSerializer(serializers.ModelSerializer):
    rewiews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'rewiews']
