import stripe
from celery import shared_task


@shared_task
def create_donation(user_channel_id: str):
    pass


@shared_task
def process_donation(donation_id: str):
    pass


@shared_task
def send_donation_receipt(donation_id: str):
    pass


@shared_task
def generate_donation_report(start_date: str, end_date: str):
    pass


@shared_task
def refund_donation(donation_id: str, reason: str):
    pass


@shared_task
def create_notification(donation_id: str):
    pass
