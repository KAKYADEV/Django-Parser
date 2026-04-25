from django.contrib import admin
from .models import ReqSite, ParsedData


class ParsedDataInline(admin.StackedInline):
    model = ParsedData
    extra = 0
    readonly_fields = ('title', 'description', 'keywords', 'time_response', 'duration_time')

@admin.register(ReqSite)
class ReqSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'status', 'time_request', 'user')
    list_filter = ('status', 'user')
    search_fields = ('name', 'url')
    ordering = ('-time_request',)
    readonly_fields = ('status', 'time_request')

    inlines = [ParsedDataInline]

@admin.register(ParsedData)
class ParsedDataAdmin(admin.ModelAdmin):
    list_display = ('site', 'title', 'description', 'keywords', 'time_response', 'duration_time')
    list_filter = ('time_response',)
    search_fields = ('site__name', 'title')
    ordering = ('-time_response',)
    readonly_fields = ('site', 'title', 'description', 'keywords', 'time_response', 'duration_time')
