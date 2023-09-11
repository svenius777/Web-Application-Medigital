from django.contrib import admin

from .models import *
# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Doktor


class CustomUserAdmin(UserAdmin):
    list_display = ("username","email", "is_staff", "is_active", "opis_doktora", "iskustvo_doktora", "dom_zdravlja", "specijalizacija_doktora", "first_name", "last_name")
    list_filter = ("username","email", "is_staff", "is_active", "opis_doktora", "iskustvo_doktora", "dom_zdravlja", "specijalizacija_doktora", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions", "opis_doktora",
                                    "iskustvo_doktora", "dom_zdravlja", "specijalizacija_doktora", "first_name", "last_name")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "first_name", "last_name", "email", 
                "specijalizacija_doktora", "opis_doktora", "iskustvo_doktora", "dom_zdravlja", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Doktor, CustomUserAdmin)
admin.site.register(Narudzba)
admin.site.register(DomZdravlja)
admin.site.register(MedicinskaSestra)


