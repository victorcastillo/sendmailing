from django.db import models
from jsonfield import JSONField

# Create your models here.


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_url_extraction = models.URLField()
    service_url_notification_id = models.URLField()
    enabled = models.BooleanField(default=True)


class Inbox(models.Model):
    service = models.ForeignKey('Service')
    id_mail_service = models.CharField(max_length=100)
    html = models.TextField()
    subject = models.CharField(max_length=100)
    from_email = models.EmailField()
    from_name = models.CharField(max_length=100)
    important = models.BooleanField(default=True)
    track_opens = models.BooleanField(default=False)
    track_clicks = models.BooleanField(default=False)
    preserve_recipients = models.BooleanField(default=False)
    tags = JSONField(null=True)
    to = JSONField()
    sent = models.BooleanField(default=False)
    reject_reason = models.CharField(max_length=40, null=True)
    id_mailing = models.TextField()
    response_mail_service = JSONField(null=True)
    notified = models.BooleanField(default=False)
