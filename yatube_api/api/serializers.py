from rest_framework import serializers
from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        view = self.context.get('view')
        post_id = view.kwargs['post_id'] if view else None
        validated_data['post'] = get_object_or_404(Post, pk=post_id)
        return super().create(validated_data)
