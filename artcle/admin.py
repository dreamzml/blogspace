from django.contrib import admin
from artcle.models import DrArtcle, DrCategory

class DrArtcleAdmin(admin.ModelAdmin):
    list_display = ('art_title','art_id', 'art_author', 'art_summary', 'inputtime')
    ordering = ('-inputtime',)
    search_fields = ('art_title',)
admin.site.register(DrArtcle, DrArtcleAdmin)

class DrCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(DrCategory, DrCategoryAdmin)
