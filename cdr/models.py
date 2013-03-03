# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class CDR(models.Model):
    u"""
    Модель для работы с CDR
    """
    calldate = models.DateTimeField(db_index=True) # datetime NOT NULL default '0000-00-00 00:00:00',
    clid = models.CharField(max_length=80, default='', db_index=True)         # varchar(80) NOT NULL default '',
    src = models.CharField(max_length=80, default='', db_index=True)          # varchar(80) NOT NULL default '',
    dst = models.CharField(max_length=80, default='', db_index=True)          # varchar(80) NOT NULL default '',
    dcontext = models.CharField(max_length=80, default='')     # varchar(80) NOT NULL default '',
    channel = models.CharField(max_length=80, default='')      # varchar(80) NOT NULL default '',
    dstchannel = models.CharField(max_length=80, default='')   # varchar(80) NOT NULL default '',
    lastapp = models.CharField(max_length=80, default='')      # varchar(80) NOT NULL default '',
    lastdata = models.CharField(max_length=200, default='')    # varchar(80) NOT NULL default '',
    duration = models.IntegerField(default=0)                  # int(11) NOT NULL default '0',
    billsec = models.IntegerField(default=0)                   # int(11) NOT NULL default '0',
    disposition = models.CharField(max_length=45, default='')  # varchar(45) NOT NULL default '',
    amaflags = models.IntegerField(default=0)                  # int(11) NOT NULL default '0',
    accountcode = models.CharField(max_length=20, default='')  # varchar(20) NOT NULL default '',
    uniqueid = models.CharField(max_length=32, default='')     # varchar(32) NOT NULL default '',
    userfield = models.CharField(max_length=255, default='')   # varchar(255) NOT NULL default ''
    peeraccount = models.CharField(max_length=20, default='')  # varchar(20) NOT NULL default ''
    linkedid = models.CharField(max_length=32, default='')     # varchar(32) NOT NULL default ''
    sequence = models.IntegerField(default=0)                  # int(11) NOT NULL default '0'

    class Meta:
        verbose_name = _('CDR')
        verbose_name_plural = _('CDRs')
        db_table = 'cdr'
        permissions = (
                   ('can_view_cdr', _('Can view on site')),
        )

    def __unicode__(self):
        return u'%s - %s - %s' % (self.calldate, self.clid, self.dst,)
