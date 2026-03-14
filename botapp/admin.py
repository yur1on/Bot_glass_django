from datetime import timedelta

from django.contrib import admin, messages
from django.utils import timezone

from .models import User, Message as BotMessage, BlockedUser, SizeSearch, PaymentEvent


# ---------- actions: подписка ----------
@admin.action(description="⭐ Добавить +30 дней подписки")
def action_add_30(modeladmin, request, queryset):
    now = timezone.now()
    for u in queryset:
        base = u.subscribed_until if (u.subscribed_until and u.subscribed_until > now) else now
        u.subscribed_until = base + timedelta(days=30)
        u.save(update_fields=["subscribed_until"])
    modeladmin.message_user(request, "Готово: +30 дней.", level=messages.SUCCESS)


@admin.action(description="⭐ Добавить +90 дней подписки")
def action_add_90(modeladmin, request, queryset):
    now = timezone.now()
    for u in queryset:
        base = u.subscribed_until if (u.subscribed_until and u.subscribed_until > now) else now
        u.subscribed_until = base + timedelta(days=90)
        u.save(update_fields=["subscribed_until"])
    modeladmin.message_user(request, "Готово: +90 дней.", level=messages.SUCCESS)


@admin.action(description="⭐ Добавить +365 дней подписки")
def action_add_365(modeladmin, request, queryset):
    now = timezone.now()
    for u in queryset:
        base = u.subscribed_until if (u.subscribed_until and u.subscribed_until > now) else now
        u.subscribed_until = base + timedelta(days=365)
        u.save(update_fields=["subscribed_until"])
    modeladmin.message_user(request, "Готово: +365 дней.", level=messages.SUCCESS)


@admin.action(description="❌ Снять подписку (обнулить)")
def action_revoke_subscription(modeladmin, request, queryset):
    queryset.update(subscribed_until=None)
    modeladmin.message_user(request, "Подписка снята.", level=messages.WARNING)


# ---------- actions: блок ----------
@admin.action(description="🚫 Заблокировать выбранных пользователей")
def action_block_users(modeladmin, request, queryset):
    created = 0
    for u in queryset:
        _, was_created = BlockedUser.objects.get_or_create(user_id=u.chat_id)
        if was_created:
            created += 1
    modeladmin.message_user(request, f"Заблокировано (новых записей): {created}", level=messages.SUCCESS)


@admin.action(description="✅ Разблокировать выбранных пользователей")
def action_unblock_users(modeladmin, request, queryset):
    ids = list(queryset.values_list("chat_id", flat=True))
    deleted, _ = BlockedUser.objects.filter(user_id__in=ids).delete()
    modeladmin.message_user(request, f"Разблокировано записей: {deleted}", level=messages.SUCCESS)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "name", "city", "phone_number", "is_subscribed", "subscribed_until")
    search_fields = ("chat_id", "name", "city", "phone_number")
    list_filter = ("city",)
    actions = [
        action_add_30,
        action_add_90,
        action_add_365,
        action_revoke_subscription,
        action_block_users,
        action_unblock_users,
    ]

    # ✅ главное: subscribed_until редактируем прямо в списке/карточке => "любое время"
    list_editable = ("subscribed_until",)

    @admin.display(boolean=True, description="subscribed")
    def is_subscribed(self, obj: User):
        return bool(obj.subscribed_until and obj.subscribed_until > timezone.now())


@admin.register(PaymentEvent)
class PaymentEventAdmin(admin.ModelAdmin):
    list_display = ("created_at", "chat_id", "event_type", "amount", "currency", "charge_id", "payload_short")
    search_fields = ("chat_id", "event_type", "charge_id", "payload")
    list_filter = ("event_type", "currency", "created_at")
    ordering = ("-created_at",)

    @admin.display(description="payload")
    def payload_short(self, obj: PaymentEvent):
        p = obj.payload or ""
        return (p[:80] + "…") if len(p) > 80 else p


@admin.register(BotMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "timestamp", "short_text")
    search_fields = ("chat_id", "message_text")
    list_filter = ("timestamp",)
    ordering = ("-timestamp",)

    @admin.display(description="text")
    def short_text(self, obj):
        t = obj.message_text or ""
        return (t[:80] + "…") if len(t) > 80 else t


@admin.register(BlockedUser)
class BlockedUserAdmin(admin.ModelAdmin):
    list_display = ("user_id",)
    search_fields = ("user_id",)


@admin.register(SizeSearch)
class SizeSearchAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "height", "width", "found_count", "source", "timestamp")
    search_fields = ("chat_id", "source")
    list_filter = ("source", "timestamp")
    ordering = ("-timestamp",)