import openai
from django.shortcuts import render, redirect

from chatSynthia.settings import OPENAI_KEY
from main_chat.models import ChatGptBot


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

            bot_response = completion['choices'][0]['text']

            obj, created = ChatGptBot.objects.get_or_create(
                user=request.user,
                messageInput=clean_user_prompt,
                bot_response=bot_response.strip(),
            )
            return redirect(request.META['HTTP_REFERER'])
        else:
            # retrieve all messages belong to logged in user
            get_history = ChatGptBot.objects.filter(user=request.user)
            context = {'get_history': get_history}
            return render(request, 'main_chat/chat.html', context)
    else:
        return redirect("users:login")
