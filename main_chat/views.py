import requests

import openai

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile

from chatSynthia.settings import OPENAI_KEY
from main_chat.models import ChatGptBot, ChatGptBotImage


# Create your views here.
def chat_text_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            openai.api_key = OPENAI_KEY
            client = openai.OpenAI()
            user_input = request.POST.get('user-input')
            clean_user_prompt = str(user_input).strip()

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": f"{clean_user_prompt}"},
                ]
            )

            bot_response = completion.choices[0].message.content

            obj, created = ChatGptBot.objects.get_or_create(
                user=request.user,
                messageInput=clean_user_prompt,
                bot_response=bot_response.strip(),
            )
            return redirect(request.META['HTTP_REFERER'])
        else:
            get_history = ChatGptBot.objects.filter(user=request.user)
            context = {'get_history': get_history}
            return render(request, 'main_chat/chat.html', context)
    else:
        return redirect("users:login")


def chat_image_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            openai.api_key = OPENAI_KEY
            client = openai.OpenAI()
            user_input = request.POST.get('user-input')
            clean_user_prompt = str(user_input).strip()

            response = client.images.generate(
                model="dall-e-3",
                prompt=clean_user_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url

            response = requests.get(image_url)
            img_file = ContentFile(response.content)

            count = ChatGptBotImage.objects.count() + 1
            fname = f'image-{count}.jpg'

            obj = ChatGptBotImage(user=request.user, messageInput=clean_user_prompt)
            obj.bot_image.save(fname, img_file)
            obj.save()

            return redirect(request.META['HTTP_REFERER'])
        else:
            get_history = ChatGptBotImage.objects.filter(user=request.user)
            context = {'get_history': get_history}
            return render(request, 'main_chat/image_chat.html', context)
    else:
        return redirect("users:login")


def delete_history_by_model(request, model):
    chatGptobj = model.objects.filter(user=request.user)
    chatGptobj.delete()
    return redirect(request.META['HTTP_REFERER'])

@login_required
def delete_history(request):
    return delete_history_by_model(request, ChatGptBot)

@login_required
def delete_history_images(request):
    return delete_history_by_model(request, ChatGptBotImage)
