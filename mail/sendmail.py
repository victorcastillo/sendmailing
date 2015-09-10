# encoding: utf-8
import mandrill
from django.conf import settings
from django.utils.encoding import force_unicode
from mail.models import Inbox


class Sendmail(object):
    def __init__(self):
        self.cliente_mandrill = mandrill.Mandrill(settings.API_KEY_MANDRILL)

    def send_message(
        self, service, id_mail_service, html, subject, from_email, from_name, to, tags,
            important=True, track_opens=False, track_clicks=False, preserve_recipients=False, **kwargs):
        data_to_send = {
            'html': html,
            'subject': force_unicode(subject),
            'from_email': from_email,
            'from_name': force_unicode(from_name),
            'important': important,
            'track_opens': track_opens,
            'track_clicks': track_clicks,
            'preserve_recipients': preserve_recipients,
            'to': to,
            'tags': tags
        }
        data_to_send.update(kwargs)
        inbox = Inbox.objects.create(service=service, id_mail_service=id_mail_service, **data_to_send)
        mandrill_response = self.cliente_mandrill.messages.send(message=data_to_send)
        inbox.response_mail_service = mandrill_response
        inbox.sent = True
        if type(mandrill_response) is dict:
            inbox.reject_reason = mandrill_response.get('message', '')
        else:
            inbox.id_mailing = mandrill_response[0].get('_id')
        inbox.save()
        return inbox
