from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet

from .models import Artwork, ArtworkImage


# 1️⃣ Custom Inline FormSet (DEFINE FIRST)
class ArtworkImageInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        primary_count = 0

        for form in self.forms:
            if not form.cleaned_data or form.cleaned_data.get("DELETE"):
                continue

            if form.cleaned_data.get("is_primary"):
                primary_count += 1

        if primary_count > 1:
            raise ValidationError(
                "Only ONE image can be marked as primary for an artwork."
            )


# 2️⃣ Inline Admin
class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1
    formset = ArtworkImageInlineFormSet


# 3️⃣ Artwork Admin
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "price", "is_for_sale", "is_auction", "year")
    list_filter = ("is_for_sale", "is_auction", "year")
    search_fields = ("title", "artist_user_first_name")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ArtworkImageInline]
