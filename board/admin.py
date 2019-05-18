from django.contrib import admin
from .models import Board
from video_encoding.admin import FormatInline
from .models import Video
# Register your models here.
admin.site.register(Board)

# @admin.register(Video)
#     class VideoAdmin(admin.ModelAdmin):
#     inlines = (FormatInline,)

#     list_dispaly = ('get_filename', 'width', 'height', 'duration')
#     fields = ('file', 'width', 'height', 'duration')
#     readonly_fields = fields