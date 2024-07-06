from django.contrib import admin
from .models import product, Category, Profile
# Register your models here.
from django.contrib.auth.models import User

admin.site.register(product)
admin.site.register(Category)
admin.site.register(Profile)


class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model


class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]
	

admin.site.unregister(User)

admin.site.register(User, UserAdmin)






