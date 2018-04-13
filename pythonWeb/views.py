from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# login_required()함수는 데코레이터로 사용되는 함수로, 일반 함수에 적용
# 사용자가 로그인 했는지를 확인해 로그인한 경우는 원래 함수로 실행하고, 로그인 되지 않은 경우는 로그인 페이지로 리다이렉트.
from django.contrib.auth.decorators import login_required

# Create your views here

# --- Homepage View
class HomeView(TemplateView):
    template_name = 'home.html'


# --- UserCreation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls,**initkwargs):
        view = super(LoginRequiredMixin,cls).as_view(**initkwargs)
        return login_required(view)