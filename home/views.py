from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView

from home.models import Product, Photo
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from home.form import ProductForm

class UserCreateView(CreateView) :
    template_name = 'login.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView) :
    template_name = 'login.html'




def HomeView(request):
    new_arrival = Product.objects.all().order_by('-create_date')[:8]
    discount = Product.objects.order_by('-create_date').filter(choice_field='Discount')[:4]
    #filtered_product_by_pk = Product.objects.filter(Product.pk)
    a = new_arrival
    sale = Product.objects.order_by('-create_date').filter(choice_field='Sale')[:1]
    time_sale = Product.objects.order_by('-create_date').filter(choice_field='TimeSale')[:1]
    context = { 'Product' : new_arrival,
                'Discount' : discount,
                'Sale' : sale,
                'TimeSale': time_sale,
                }
    return render(request, 'index.html', context)


def Single_product(request, pk):
    photo = Photo.objects.filter(product__pk = pk)
    print(request.method)
    product = get_object_or_404(Product, pk=pk)
    object = Product.objects.get(pk=pk)
    if request.method == "POST":
       form = ProductForm(request.POST, instance=object)
       if form.is_valid():
            rating = form.save(commit=False)
            rating.save()
            return redirect(object)
       else :
            print("cccc" + form.errors)

    else :
        form = ProductForm()

    context = { 'Photo' : photo,
                'Product' : product,
                'Rating' :form
                }
    return render(request, 'single-product.html', context)

