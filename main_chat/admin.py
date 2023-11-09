from django.contrib import admin

from main_chat.models import ChatGptBot, ChatGptBotImage


# Register your models here.
@admin.register(ChatGptBot)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('user', 'messageInput', 'bot_response')


@admin.register(ChatGptBotImage)
class ChatGptBotImageAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('user', 'messageInput', 'bot_image')
