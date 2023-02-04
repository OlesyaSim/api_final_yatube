from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())
    user = SlugRelatedField(slug_field='username', read_only=True,
                            default=serializers.CurrentUserDefault())

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                fields=['user', 'following'],
                queryset=Follow.objects.all(),
                message='Вы уже подписаны на этого автора!'
            )]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться на самого '
                                              'себя!')
        return value
