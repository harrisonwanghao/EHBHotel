from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from products.forms import ProductAddForm
from products.models import Product


def ProductAdd(request):
    if request.user.is_authenticated and request.user.ad:
        if request.method == 'POST':
            form = ProductAddForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/products/')
            else:
                return render_to_response('addproduct.html', {'form': form}, context_instance=RequestContext(request))

        else:
            form = ProductAddForm()
            context = {'form': form}
            return render_to_response('addproduct.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def ProductList(request):
    if request.user.is_authenticated and request.user.ad:
        return render_to_response('products.html', {'products': Product.objects.all()}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')
