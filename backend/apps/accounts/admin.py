from django.contrib import admin
from .models import User, ArtistProfile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ("role",)
    search_fields = ('email',)

@admin.register(ArtistProfile)
class ArtistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', "first_name", 'last_name','membership_plan')
    search_fields = ('user__email', 'first_name', 'last_name')
    prepopulated_fields = {"slug": ("first_name", "last_name")}
