from rest_framework import serializers

from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = '__all__'
        # will take all fields relevant to Post

    # будет собирать один объект
    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["user"] = instance.user.username

        dict_["likes"] = instance.likes.all().count()

        dict_["comments"] = CommentSerializer(instance.comments.all(), many=True).data

        return dict_

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        # fields = '__all__'
        # те поля которые не будут включаться 
        exclude = ['post']

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["user"] = instance.user.username
        return dict_

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__' 