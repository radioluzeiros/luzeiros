from django.contrib import admin
from luzeiros.blog.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at', 'updated_at']

    # Ensure applications cannot write in admin site
    def has_add_permission(self, request):
        return not request.user.is_app or not request.user.is_active

    def has_change_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active

    def has_delete_permission(self, request, obj=None):
        return not request.user.is_app or not request.user.is_active
