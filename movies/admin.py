from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Hero, Rating, RatingStar, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url",)
    list_display_links = ("name", )

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    #fields = (("heroes", "directors", "genre"), )
    fieldsets = (
        (None, {
            "fields": (("title", "japantitle"),)
        }),
        (None, {
            "fields": (("country", "year"),)
        }),
        (None, {
            "fields": (("description", "poster"),)
        }),
        ("Режисер", {
            "classes": ("collapse",),
            "fields": (("heroes", "genre", "directors"),)
        }),
        (None, {
            "fields": (("word_premiere", "budget", "category"),)
        }),
        ("Опционально", {
            "fields": (("url", "draft"),)
        }),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """жанры"""
    list_display = ("name", "description", "url")

@admin.register(MovieShots)
class MovieShots(admin.ModelAdmin):
    """карды и аниме"""
    list_display = ("title", "description", "image", "movie")

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    """герои"""
    list_display = ("name", "description", "image", "age")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("ip", "star", "movie")

@admin.register(RatingStar)
class RatingAdmin(admin.ModelAdmin):
    """Звезды рейтинга"""
    list_display = ("value",)




