from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Author, Category, Post, Comment, PostView


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)


class UserInline(admin.StackedInline):
    model = Author
    can_delete = True
    verbose_name = Author

class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )



