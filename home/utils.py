from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import logging

logger = logging.getLogger(__name__)

def send_verification_email(user):
    try:
        subject = 'Verify your email address'
        message = render_to_string('emails/verify_email.html', {
            'user': user,
            'verification_url': f"{settings.SITE_URL}/verify-email/{user.email_verification_token}"
        })
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=message,
        )
        logger.info(f"Verification email sent to {user.email}")
    except Exception as e:
        logger.error(f"Failed to send verification email to {user.email}: {str(e)}")

def send_password_reset_email(user, token):
    try:
        subject = 'Reset your password'
        message = render_to_string('emails/reset_password.html', {
            'user': user,
            'reset_url': f"{settings.SITE_URL}/reset-password/{token}"
        })
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=message,
        )
        logger.info(f"Password reset email sent to {user.email}")
    except Exception as e:
        logger.error(f"Failed to send password reset email to {user.email}: {str(e)}")