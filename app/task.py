from celery import shared_task


@shared_task
def add_to_cart(user_id: int, product_id: int, quantity: int):
    pass
