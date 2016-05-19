from django.contrib import admin
from cms.models import Book, Impression

# admin.site.register(Book)
# admin.site.register(Impression)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # $B0lMw$K=P$7$?$$9`L\(B
    list_display_links = ('id', 'name',)  # $B=$@5%j%s%/$G%/%j%C%/$G$-$k9`L\(B
admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
admin.site.register(Impression, ImpressionAdmin)
