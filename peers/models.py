# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
try:
    from asterctl.settings import PEER_DB
except ImportError:
    PEER_DB = 'peers'

PEER_TYPES = (('friend', 'friend',)
              , ('user', 'user',)
              , ('peer', 'peer',),
              )

DTMF_MODES = (('rfc2833', 'rfc2833',)
             , ('info', 'info',)
             , ('shortinfo', 'shortinfo',)
             , ('inband', 'inband',)
             , ('auto', 'auto',),
             )
YESNO_CHOICE = (('yes', 'Yes',)
                , ('no', 'No',),
                )
TRANSPORT = (('udp', 'udp',)
            , ('tcp', 'tcp',)
            , ('udp,tcp', 'udp,tcp',)
            , ('tcp,udp', 'tcp,udp',),
            )
INSECURE = (('invite', 'invite',)
            , ('port', 'port',)
            , ('port,invite', 'port,invite',),)
SESSION_TIMERS = (('accept', 'accept',)
                  , ('refuse', 'refuse',)
                  , ('originate', 'originate',),)
SESSION_REFRESHER = (('uac', 'uac',), ('uas', 'uas',),)
CALLINGPRES = (('allowed_not_screened', 'allowed_not_screened',)
               , ('allowed_passed_screen', 'allowed_passed_screen',)
               , ('allowed_failed_screen', 'allowed_failed_screen',)
               , ('allowed', 'allowed',)
               , ('prohib_not_screened', 'prohib_not_screened',)
               , ('prohib_passed_screen', 'prohib_passed_screen',)
               , ('prohib_failed_screen', 'prohib_failed_screen',)
               , ('prohib', 'prohib',),
               )
class Peer(models.Model):
    u"""
    Модель пира
    """
    name = models.CharField(max_length=40)
    ipaddr = models.IPAddressField(max_length=45
                                   , blank=True
                                   , editable=False
                                   , default='')
    port = models.IntegerField(max_length=5
                               , blank=True
                               , editable=False
                               , default=0)
    regseconds = models.IntegerField(max_length=11
                                     , blank=True
                                     , editable=False
                                     , default=0)
    defaultuser = models.CharField(max_length=40, blank=True, null=True)
    fullcontact = models.CharField(max_length=35, blank=True, editable=False)
    regserver = models.CharField(max_length=20, blank=True, editable=False)
    useragent = models.CharField(max_length=20, blank=True, editable=False)
    lastms = models.IntegerField(max_length=11, blank=True, editable=False)

    host = models.CharField(max_length=40, blank=True, default='dynamic')
    peer_type = models.CharField(db_column='type'
                                 , max_length=10
                                 , choices=PEER_TYPES
                                 , blank=True
                                 , null=True
                                 , default='friend')
    context = models.CharField(max_length=40)
    deny = models.CharField(max_length=40, blank=True, null=True
                            , help_text="format: <em>XXX.XXX.XXX.XXX/XXX.XXX.XXX.XXX</em>.")
    permit = models.CharField(max_length=40, blank=True, null=True
                              , help_text="format: <em>XXX.XXX.XXX.XXX/XXX.XXX.XXX.XXX</em>.")
    secret = models.CharField(max_length=40)
    md5secret = models.CharField(max_length=40, blank=True, null=True)
    remotesecret = models.CharField(max_length=40, blank=True, null=True)

    transport = models.CharField(max_length=7
                                 , choices=TRANSPORT
                                 , blank=True
                                 , null=True)
    dtmfmode = models.CharField(max_length=10
                                , choices=DTMF_MODES
                                , blank=True
                                , null=True
                                , default='rfc2833')
    directmedia = models.CharField(max_length=10
                                , choices=YESNO_CHOICE+(('nonat', 'nonat')
                                                        , ('update', 'update'),)
                                , blank=True
                                , null=True)
    nat = models.CharField(max_length=10
                                , choices=YESNO_CHOICE+(('never', 'never')
                                                        , ('route', 'route'),)
                                , blank=True
                                , null=True)

    callgroup = models.CharField(max_length=40, blank=True, null=True)
    pickupgroup = models.CharField(max_length=40, blank=True, null=True)

    language = models.CharField(max_length=40, blank=True, null=True, default='ru')

    disallow = models.CharField(max_length=40, blank=True, null=True, default='all')
    allow = models.CharField(max_length=40, blank=True, null=True, default='ulaw,alaw')

    insecure = models.CharField(max_length=40
                                , choices=INSECURE
                                , blank=True
                                , null=True)
    trustrpid = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    progressinband = models.CharField(max_length=10
                                , choices=YESNO_CHOICE+(('never', 'never'),)
                                , blank=True
                                , null=True)
    promiscredir = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    useclientcode = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)

    accountcode = models.CharField(max_length=40, blank=True, null=True)
    setvar = models.CharField(max_length=40, blank=True, null=True)
    callerid = models.CharField(max_length=40, blank=True, null=True)
    amaflags = models.CharField(max_length=40, blank=True, null=True)

    callcounter = models.CharField(max_length=10
                                   , choices=YESNO_CHOICE
                                   , blank=True
                                   , null=True
                                   , default='yes')
    busylevel = models.IntegerField(max_length=11, blank=True, null=True, default=1)

    allowoverlap = models.CharField(max_length=10
                                   , choices=YESNO_CHOICE
                                   , blank=True
                                   , null=True)
    allowsubscribe = models.CharField(max_length=10
                                   , choices=YESNO_CHOICE
                                   , blank=True
                                   , null=True
                                   , default='no')
    videosupport = models.CharField(max_length=10
                                   , choices=YESNO_CHOICE
                                   , blank=True
                                   , null=True
                                   , default='no')
    maxcallbitrate = models.IntegerField(max_length=11, blank=True, null=True)
    rfc2833compensate = models.CharField(max_length=10
                                   , choices=YESNO_CHOICE
                                   , blank=True
                                   , null=True)
    mailbox = models.CharField(max_length=40, blank=True, null=True)

    session_timers = models.CharField(db_column='session-timers'
                                      , max_length=40
                                      , choices=SESSION_TIMERS
                                      , blank=True
                                      , null=True)
    session_expires = models.IntegerField(db_column='session-expires'
                                     , max_length=11
                                     , blank=True
                                     , null=True)
    session_minse = models.IntegerField(db_column='session-minse'
                                     , max_length=11
                                     , blank=True
                                     , null=True)
    session_refresher = models.CharField(db_column='session-refresher'
                                        , max_length=40
                                        , choices=SESSION_REFRESHER
                                        , blank=True
                                        , null=True)
    t38pt_usertpsource = models.CharField(max_length=40, blank=True, null=True)
    regexten = models.CharField(max_length=40, blank=True, null=True)
    fromdomain = models.CharField(max_length=40, blank=True, null=True)
    fromuser = models.CharField(max_length=40, blank=True, null=True)
    qualify = models.CharField(max_length=40, blank=True, null=True)
    defaultip = models.CharField(max_length=40, blank=True, null=True)
    rtptimeout = models.IntegerField(max_length=11, blank=True, null=True)
    rtpholdtimeout = models.IntegerField(max_length=11, blank=True, null=True)
    sendrpid = models.CharField(max_length=10
                                , choices=YESNO_CHOICE+(('pai', 'pai'),)
                                , blank=True
                                , null=True)
    outboundproxy = models.CharField(max_length=40, blank=True, null=True)
    callbackextension = models.CharField(max_length=40, blank=True, null=True)

    timert1 = models.IntegerField(max_length=11, blank=True, null=True)
    timerb = models.IntegerField(max_length=11, blank=True, null=True)
    qualifyfreq = models.IntegerField(max_length=11, blank=True, null=True)

    constantssrc = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)

    contactdeny = models.CharField(max_length=40, blank=True, null=True
                                   , help_text="format: <em>XXX.XXX.XXX.XXX/XXX.XXX.XXX.XXX</em>.")
    contactpermit = models.CharField(max_length=40, blank=True, null=True
                                     , help_text="format: <em>XXX.XXX.XXX.XXX/XXX.XXX.XXX.XXX</em>.")

    usereqphone = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='yes')
    textsupport = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='no')
    faxdetect = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='no')
    buggymwi = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='no')

    auth = models.CharField(max_length=40, blank=True, null=True)
    fullname = models.CharField(max_length=40)
    trunkname = models.CharField(max_length=40, blank=True, null=True)
    cid_number = models.CharField(max_length=40, blank=True, null=True)
    callingpres = models.CharField(max_length=40
                                    , choices=CALLINGPRES
                                    , blank=True
                                    , null=True)
    mohinterpret = models.CharField(max_length=40, blank=True, null=True)
    mohsuggest = models.CharField(max_length=40, blank=True, null=True)
    parkinglot = models.CharField(max_length=40, blank=True, null=True)

    hasvoicemail = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='no')
    subscribemwi = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True
                                , default='no')
    vmexten = models.CharField(max_length=40, blank=True)
    autoframing = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    rtpkeepalive = models.IntegerField(max_length=11, blank=True, null=True)

    call_limit = models.IntegerField(db_column='call-limit'
                                     , max_length=11
                                     , blank=True
                                     , null=True
                                     , default=1)
    g726nonstandard = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    ignoresdpversion = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    allowtransfer = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    dynamic = models.CharField(max_length=10
                                , choices=YESNO_CHOICE
                                , blank=True
                                , null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    date_add = models.DateTimeField(editable=False
                                    , auto_now=True
                                    , auto_now_add=True)

    class Meta:
        verbose_name= _('Peer')
        verbose_name_plural = _('Peers')
        db_table = PEER_DB
        permissions = (
                   ('can_view_sippeer', _('Can view on site')),
        )

    def __unicode__(self):
        return self.name

    def is_online(self):
        if self.port > 0: return True
        return False
    is_online.boolean = True
