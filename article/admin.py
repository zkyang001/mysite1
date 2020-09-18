from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("pk", "title", "content", "last_update_time", "author",)
	ordering = ("pk",)

# admin.site.register(models.Article, ArticleAdmin)

