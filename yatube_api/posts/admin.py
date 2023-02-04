from django.contrib import admin

from .models import Comment, Follow, Group, Post


# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Follow)
# admin.site.register(Group)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'following', 'user')
    list_filter = ('following', 'user')
    search_fields = ('text',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
    search_fields = ('description', 'title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created')
    list_filter = ('author', )
    search_fields = ('post', 'text')
