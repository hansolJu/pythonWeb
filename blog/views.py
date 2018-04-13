from django.views.generic import ListView, DetailView, TemplateView, \
    CreateView, UpdateView, DeleteView

from django.views.generic.dates import ArchiveIndexView, \
    YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy

from blog.models import Post
from pythonWeb.views import LoginRequiredMixin


# Create your views here.
# --- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'


# --- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# --- DetailView
class PostDV(DetailView):
    model = Post


# --- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


# --- FromView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        # icontains = 대소문자구분없이 검색
        post_list = Post.objects.filter(
            Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)  # No Redirection


# --- CRUD View
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = {'slug': 'auto-filling-do-not-input'}
    # slug 필드를 처리하는 또 다른 방법은 fields속성에서 제외해 폼에 나타나지 않도록 하는 방법입니다. \
    # 폼에는 보이지 않지만, Post 모델의 save()함수에 의해 테리블의 레코드에는 자동으로 채워집니다.
    # fields = ['title', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    success_url = reverse_lazy('blog:index')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')
