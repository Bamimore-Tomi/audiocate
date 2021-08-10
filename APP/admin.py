from django.contrib import admin
from . models import Book,Genre,Explore,UserProfile,Featured



# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Explore)
admin.site.register(UserProfile)
admin.site.register(Featured)
