from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Consultation)
admin.site.register(Tool)
admin.site.register(Review)