from django.contrib import admin


from .models import Genre, Movie

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ["name","date","genre","grossing","budget"]
    list_display_links = ["name"]
    date_hierarchy = 'date'
    list_per_page = 20
    list_filter = ['date','genre']
    search_fields = ['name']
    list_editable = ['grossing','budget','date']

    class Meta:
        model = Movie


admin.site.register(Movie,MovieModelAdmin)
admin.site.register(Genre)
