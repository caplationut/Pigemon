from datetime import datetime

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import mail_admins

from pigeon.models import Pigeon, ClaimRequest

CLAIM_REQUEST_EMAIL_SUBJECT = 'New claim request'
CLAIM_REQUEST_EMAIL_TEMPLATE = 'email/claim_request.txt'


@receiver(pre_save, sender=Pigeon)
def pigeon_status_change_callback(sender, **kwargs):
    """Update event_date field when status field is changed."""
    if kwargs['instance'].id:
        prev_data = sender.objects.get(pk=kwargs['instance'].id)
        if prev_data.status != kwargs['instance'].status:
            kwargs['instance'].event_date = datetime.now()


@receiver(pre_save, sender=ClaimRequest)
def pre_save_claim_request(sender, instance, **kwargs):
    other_requests = ClaimRequest.objects.filter(
        pigeon=instance.pigeon,
        status__in=[
            ClaimRequest.Status.OPEN,
            ClaimRequest.Status.ACCEPTED
        ]).count()
    if other_requests:
        raise Exception('has_claim_requests')


@receiver(post_save, sender=ClaimRequest)
def post_save_claim_request(sender, instance, **kwargs):
    """Send email to admins for each new claim request."""
    if instance.id:
        context = {
            'initiator': instance.initiator,
            'ring_serial': instance.pigeon.ring_serial,
            'id': instance.id
        }
        message = render_to_string(CLAIM_REQUEST_EMAIL_TEMPLATE, context)
        mail_admins(
            CLAIM_REQUEST_EMAIL_SUBJECT,
            message,
            True
        )
