from django.views.generic import ListView,DetailView
from photo.models import Album,Photo

from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from pythonWeb.views import LoginRequiredMixin
# Create your views here.


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo


# --- CRUD for Photo
class PhotoCreateView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['album','title','image','description']
    success_url = reverse_lazy('photo:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PhotoCreateView,self).form_valid(form)


class PhotoChangeLV(LoginRequiredMixin,ListView):
    model = Photo
    template_name = 'photo/photo_change_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)


class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['album','title','image','description']
    success_url = reverse_lazy('photo:index')


class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = reverse_lazy('photo:index')


# --- CRUD for Album
class AlbumChangeLV(LoginRequiredMixin,ListView):
    template_name = 'photo/album_change_list.html'

    def get_queryset(self):
        return Album.objects.filter(owner=self.request.user)


class AlbumDeleteView(LoginRequiredMixin,DeleteView):
    model = Album
    success_url = reverse_lazy('photo:index')


# --- InlineFormSet View
# --- add/update for Album
from django.shortcuts import redirect
from photo.forms import PhotoInlineFormSet


class AlbumPhotoCV(LoginRequiredMixin,CreateView):
    model = Album
    fields = ['name','description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs): # 추가적인 변수 지정을 위해 오버라이딩.
        context = super(AlbumPhotoCV,self).get_context_data(**kwargs)
        if self.request.POST: # Post 요청일경우
            context['formset'] = PhotoInlineFormSet(self.request.POST,self.request.FILES)
        else: # Get 요청일경우 formset 파라미터 지정
            context['formset'] = PhotoInlineFormSet()
        return context # context 변수 사전 반환

    def form_valid(self, form): # 폼에 입력된 내용 유효성 검사후 저장
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form = form))


class AlbumPhotoUV(LoginRequiredMixin,UpdateView):
    model = Album
    fields = ['name','description']
    template_name = 'photo/album_form.html'

    def get_context_data(self, **kwargs): # 추가적인 변수 지정을 위해 오버라이딩.
        context = super(AlbumPhotoUV,self).get_context_data(**kwargs)
        if self.request.POST: # Post 요청일경우
            context['formset'] = PhotoInlineFormSet(self.request.POST,self.request.FILES,instance = self.object)
        else: # Get 요청일경우 formset 파라미터 지정
            context['formset'] = PhotoInlineFormSet(instance = self.object)
        return context # context 변수 사전 반환

    def form_valid(self, form): # 폼에 입력된 내용 유효성 검사후 저장
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form = form))