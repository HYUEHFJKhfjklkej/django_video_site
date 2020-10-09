from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Hero, Rating, RatingStar, Review


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url",)
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")

class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, object):
        return mark_safe(f'<img src={object.image.url} width="80" height="60" ')

    get_image.short_description = "Изображение"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ("get_image",)
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    form = MovieAdminForm
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("title", "japantitle"),)
        }),
        (None, {
            "fields": (("country", "year"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
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
    def get_image(self, object):
        return mark_safe(f'<img src={object.poster.url} width="80" height="60" ')

    get_image.short_description = "Постер"

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
    list_display = ("title", "description", "get_image", "movie")
    readonly_fields = ("get_image",)

    def get_image(self, object):
        return mark_safe(f'<img src={object.image.url} width="80" height="60" ')

    get_image.short_description = "Изображение"


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    """герои"""
    list_display = ("name", "description", "get_image", "age")
    readonly_fields = ("get_image",)

    def get_image(self, object):
        return mark_safe(f'<img src={object.image.url} width="80" height="60" ')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ("ip", "star", "get_image")

    def get_image(self, object):
        return mark_safe(f'<img src={object.image.url} width="80" height="60" ')

    get_image.short_description = "Изображение"


@admin.register(RatingStar)
class RatingStarsAdmin(admin.ModelAdmin):
    """Звезды рейтинга"""
    list_display = ("value",)

admin.sites.site_title = "Anichan"
admin.site.site_header = "Anichan"