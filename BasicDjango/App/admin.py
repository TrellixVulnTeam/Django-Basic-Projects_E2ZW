from django.contrib import admin
from App.models import Author, Article, Category


class AuthorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__", "details"]
    class Meta:
        Model = Author
admin.site.register(Author, AuthorModel)

class ArticleModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__", "details"]
    list_per_page = 10
    list_filter = ["posted_on", "category"]
    class Meta:
        Model = Article
admin.site.register(Article, ArticleModel)

admin.site.register(Category)