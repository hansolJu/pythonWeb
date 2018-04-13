from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bookmark.models import Bookmark
from pythonWeb.views import LoginRequiredMixin


# Create your views here.


# --- Listview
class BookmarkLV(ListView):
    model = Bookmark


# --- DetailView
class BookmarkDV(DetailView):
    model = Bookmark


# --- CRUDView
class BookmarkCreateView(LoginRequiredMixin,CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user # 현재 로그인된 사용자의 User객체를 할당.
        return super(BookmarkCreateView,self).form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin,ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    # Bookmark 테이블의 레코드중에서 owner필드가 로그인한 사용자인 레코드만 필터링해 그 리스트를 반환.
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin,UpdateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(LoginRequiredMixin,DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
