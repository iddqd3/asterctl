# -*- coding: utf-8 -*-
from django.contrib import admin
from cdr.models import CDR

class CDRAdmin(admin.ModelAdmin):
    list_display = ('calldate', 'clid', 'src', 'dst', 'dcontext', 'billsec', 'disposition',)
    list_display_links = ('calldate', 'clid', 'src', 'dst', )
    ordering = ['-calldate']
    search_fields = ('calldate', 'clid',)
    list_filter = ('calldate', 'dcontext', 'disposition',)

admin.site.register(CDR, CDRAdmin)
