from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import PostCreateForm, UploadImagesForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class BlogsView(ListView):
    model = models.Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        context.update({
            'category_context': models.Category.objects.all(),
            'region_context': models.Region.objects.all(),
        })
        return context


class BlogsDetailView(DetailView):
    model = models.Post
    template_name = 'detail.html'


def PostCreateView(request):
    if request.method == 'POST':
        images_form = UploadImagesForm(request.POST, request.FILES)
        if images_form.is_valid():
            images_form.save()
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = models.Post()
            post.name = request.POST['name']
            post.description = request.POST['description']
            post.image = models.UploadedImage.objects.get(pk=images_form.instance.id)
            post.category = models.Category.objects.get(pk=request.POST['category'])
            post.region = models.Region.objects.get(pk=request.POST['region'])
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostCreateForm()

    return render(request, 'post_form.html', {'form': form})


def BlogsByView(request, by=None, id=None):
    queryset = []
    if by == 'region':
        queryset = models.Post.objects.filter(category=id).order_by('id')
    elif by == 'category':
        queryset = models.Post.objects.filter(region=id).order_by('id')
    context = {'obj': queryset}
    return render(request, 'post-by.html', context)


def ImageCreateView(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        form = UploadImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # print(form)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UploadImagesForm()
    return render(request, 'image_create.html', {'form': form})