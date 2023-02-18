from django.contrib import admin

from .models import Comment, Like, LikeComment, Rating


class RatingAdmin(admin.ModelAdmin):
    list_filter = ['rating']
    list_display = ['author', 'rating', 'packet']
    search_fields = ['rating', 'packet']

admin.site.register(Rating, RatingAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_filter = ['packet']
    list_display = ['author', 'packet', 'is_liked']
    search_fields = ['author', 'packet']

admin.site.register(Like, LikeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['packet']
    list_display = ['author', 'packet', 'created_at', 'updated_at', 'body']
    search_fields = ['author', 'packet']

admin.site.register(Comment, CommentAdmin)


class LikeCommentAdmin(admin.ModelAdmin):
    list_filter = ['author']
    list_display = ['author', 'comment', 'is_liked']
    search_fields = ['author']

admin.site.register(LikeComment, LikeCommentAdmin)


class LikeCommentInline(admin.TabularInline):
    model = LikeComment
