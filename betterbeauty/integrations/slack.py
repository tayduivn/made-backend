import logging

from django.conf import settings
from django.template.loader import render_to_string

from slackweb import Slack

from core.constants import EnvLevel

logger = logging.getLogger(__name__)


def send_slack_message(channel: str, slack_url: str, bot_name: str, message: str):
    if not settings.IS_SLACK_ENABLED:
        return
    slack = Slack(url=slack_url)
    try:
        slack.notify(
            text=message,
            channel=channel,
            username=bot_name,
        )
    except:  # noqa
        # we really don't want this to break the flow for whatever reason
        if settings.LEVEL != EnvLevel.PRODUCTION:
            raise
        logger.exception('Failed to send Slack message to channel {}'.format(
            channel
        ), exc_info=True)


def send_slack_twilio_message_notification(from_phone, to_phone, message):
    # TODO: update context with stylist and client
    message = render_to_string(
        'slack/twilio_message_notification.txt',
        context={
            'from_phone': from_phone,
            'to_phone': to_phone,
            'message': message,
        })
    send_slack_message(
        channel=settings.TWILLIO_SLACK_CHANNEL,
        slack_url=settings.TWILLIO_SLACK_HOOK,
        bot_name='twilio-bot', message=message
    )


def send_slack_user_disabled_sms_notifications(user):
    message = render_to_string(
        'slack/user_disabled_sms_notifications.txt',
        context={
            'user': user
        })
    send_slack_message(
        channel=settings.TWILLIO_SLACK_CHANNEL,
        slack_url=settings.TWILLIO_SLACK_HOOK,
        bot_name='twilio-bot', message=message
    )


def send_slack_user_enabled_sms_notifications(user):
    message = render_to_string(
        'slack/user_enabled_sms_notifications.txt',
        context={
            'user': user
        })
    send_slack_message(
        channel=settings.TWILLIO_SLACK_CHANNEL,
        slack_url=settings.TWILLIO_SLACK_HOOK,
        bot_name='twilio-bot', message=message
    )


def send_slack_incoming_twilio_notification(user, body):
    message = render_to_string(
        'slack/incoming_twilio_notification.txt',
        context={
            'user': user,
            'body': body
        })
    send_slack_message(
        channel=settings.TWILLIO_SLACK_CHANNEL,
        slack_url=settings.TWILLIO_SLACK_HOOK,
        bot_name='twilio-bot', message=message
    )


def send_slack_new_user_signup(user):
    try:
        message = render_to_string(
            'slack/auto_signup_new_user_notification.txt',
            context={
                'user': user,
            })
        send_slack_message(
            channel=settings.AUTO_SIGNUP_SLACK_CHANNEL,
            slack_url=settings.AUTO_SIGNUP_SLACK_HOOK,
            bot_name='auto-signup-bot', message=message
        )
    except:  # noqa we *really* don't want any issues here
        pass


def send_slack_client_profile_update(client):
    try:
        message = render_to_string(
            'slack/auto_signup_client_update_notification.txt',
            context={
                'client': client,
            })
        send_slack_message(
            channel=settings.AUTO_SIGNUP_SLACK_CHANNEL,
            slack_url=settings.AUTO_SIGNUP_SLACK_HOOK,
            bot_name='auto-signup-bot', message=message
        )
    except:  # noqa we *really* don't want any issues here
        pass


def send_slack_stylist_profile_update(stylist):
    try:
        message = render_to_string(
            'slack/auto_signup_stylist_update_notification.txt',
            context={
                'stylist': stylist,
            })
        send_slack_message(
            channel=settings.AUTO_SIGNUP_SLACK_CHANNEL,
            slack_url=settings.AUTO_SIGNUP_SLACK_HOOK,
            bot_name='auto-signup-bot', message=message
        )
    except:  # noqa we *really* don't want any issues here
        pass


def send_slack_auto_booking_notification(appointment):
    try:
        message = render_to_string(
            'slack/auto_booking_notification.txt',
            context={
                'appointment': appointment,
            })
        send_slack_message(
            channel=settings.AUTO_BOOKING_SLACK_CHANNEL,
            slack_url=settings.AUTO_BOOKING_SLACK_HOOK,
            bot_name='auto-booking-bot', message=message
        )
    except:  # noqa we *really* don't want any issues here
        pass


def send_slack_email(mail):
    try:
        message = render_to_string(
            'slack/email.txt',
            context={
                'mail': mail,
            })
        send_slack_message(
            channel=settings.AUTO_EMAIL_SLACK_CHANNEL,
            slack_url=settings.AUTO_EMAIL_SLACK_HOOK,
            bot_name='auto-email-bot', message=message
        )
    except: # noqa we *really* don't want any issues here
        pass


def send_stripe_charge_notification(charge, error=None):
    message = render_to_string(
        'slack/auto_stripe_notification.txt',
        context={
            'charge': charge,
            'error': error
        })
    send_slack_message(
        channel=settings.AUTO_STRIPE_SLACK_CHANNEL,
        slack_url=settings.AUTO_STRIPE_SLACK_HOOK,
        bot_name='twilio-bot', message=message
    )
