from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from users.forms import ProfileForm, UserLoginForm, UserRegisterForm
from users.models import User


# Create your views here.
class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)


class RegistrationView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        response = super().form_valid(form)
        auth.login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with username or password, check again !')
        return super().form_invalid(form)


class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = ''

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
