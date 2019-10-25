from django.shortcuts import render, get_object_or_404
from .models import Bolgs, Bolg_type
from django.core.paginator import Paginator
# Create your views here.


def blog_list(request):
    blos_all_list = Bolgs.objects.all()
    paginator = Paginator(blos_all_list, 3)
    page_num = request.GET.get('page', 1)
    page_of_blog = paginator.get_page(page_num)
    # currentr_page_num = page_of_blog.number
    page_range = [x for x in range(int(page_num) - 2, int(page_num) + 3) if 0 < x <= paginator.num_pages]
    context = dict()
    context['page_range'] = page_range
    context['paginator'] = page_of_blog
    context['blogs'] = Bolgs.objects.all()
    context['blog_types'] = Bolg_type.objects.all()
    return render(request, 'blog_list.html', context=context)


def blog_detail(request, blog_pk):
    context = dict()
    context['blog'] = get_object_or_404(Bolgs, pk=blog_pk)
    return render(request, 'blog_detail.html', context=context)


def blog_with_type(request, blog_type_pk):
    context = dict()
    blog_type = get_object_or_404(Bolg_type, pk=blog_type_pk)
    context['blogs'] = Bolgs.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    context['blog_types'] = Bolg_type.objects.all()
    return render(request,'blogs_with_type.html', context=context)