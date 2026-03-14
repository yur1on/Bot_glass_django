from django.db import models


class User(models.Model):
    chat_id = models.BigIntegerField(unique=True, db_index=True)
    name = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)

    # ✅ подписка
    subscribed_until = models.DateTimeField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.chat_id} {self.name or ''}".strip()


class Message(models.Model):
    chat_id = models.BigIntegerField(db_index=True)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class BlockedUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)


class SizeSearch(models.Model):
    chat_id = models.BigIntegerField(db_index=True)
    height = models.FloatField()
    width = models.FloatField()
    found_count = models.IntegerField()
    source = models.TextField(default="unknown")
    timestamp = models.DateTimeField(auto_now_add=True)


class PaymentEvent(models.Model):
    """
    ✅ Лог событий оплаты/подписки:
    - нажал /subscribe
    - successful_payment
    - назначено админом вручную (если захочешь)
    """
    EVENT_CHOICES = [
        ("subscribe_click", "Subscribe click"),
        ("successful_payment", "Successful payment"),
        ("admin_grant", "Admin grant"),
        ("admin_revoke", "Admin revoke"),
    ]

    chat_id = models.BigIntegerField(db_index=True)
    event_type = models.CharField(max_length=32, choices=EVENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    # поля оплаты (заполняются только для successful_payment)
    amount = models.IntegerField(null=True, blank=True)     # Stars amount
    currency = models.CharField(max_length=8, null=True, blank=True)  # "XTR"
    charge_id = models.TextField(null=True, blank=True)

    # произвольные данные (payload, username и т.д.)
    payload = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.chat_id} {self.event_type} {self.created_at}"