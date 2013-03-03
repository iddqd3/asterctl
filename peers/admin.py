# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from peers.models import Peer

class IsOnline(SimpleListFilter):
    title = _('online')
    parameter_name = 'online'

    def lookups(self, request, model_admin):
        return (
                ('1', _('yes')),
                ('0', _('no')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(port__gt = 0)
        elif self.value() == '0':
            return queryset.filter(port__lte = 0)

class PeerAdmin(admin.ModelAdmin):
    list_display = ('context', 'name', 'fullname', 'cid_number'
                    , 'description', 'date_add', 'is_online', )
    list_display_links = ('name', 'fullname',)
    list_filter = ('peer_type', 'context', 'date_add', IsOnline,)
    search_fields = ('name', 'cid_number', )

admin.site.register(Peer, PeerAdmin)
