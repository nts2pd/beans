from django.shortcuts import render, get_object_or_404
from .models import Customer, Order
from django.views import generic
from .forms import OrderForm, OrderAgainForm
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory


class IndexView(generic.ListView):
    template_name = 'bacon/index.html'
    context_object_name = 'latest_order_list'

    def get_queryset(self):
        return Customer.objects.order_by('last_name')

class DetailView(generic.DetailView):
    model = Customer
    template_name = 'bacon/detail.html'

class OrdersView(generic.DetailView):
    model = Customer
    template_name = 'bacon/orders.html'

def place_order(request):
    customer = Customer()
    price = 0
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer.first_name = form.cleaned_data['first_name']
            customer.last_name = form.cleaned_data['last_name']
            customer.favorite_food = form.cleaned_data['favorite']
            customer.save()
            order = customer.order_set.create(entree=form.cleaned_data['entree'], side=form.cleaned_data['side'])
            if order.entree == 'HAM':
                price += 5
            elif order.entree == 'CHZ':
                price += 6
            elif order.entree == 'TAC':
                price += 3
            elif order.entree == 'FSH':
                price += 8
            else:
                price += 0
            if order.side == 'FRI':
                price += 3
            elif order.side == 'SAL':
                price += 2
            elif order.side == 'BNS':
                price += 3
            elif order.side == 'ORG':
                price += 5
            else:
                price += 0
            order.price = price
            order.save()
            return HttpResponseRedirect('/bacon/')
    else:
        form = OrderForm()
    return(render(request, 'bacon/place_order.html', {'form': form}))

def order_again(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    price = 0
    if request.method == 'POST':
        form = OrderAgainForm(request.POST)
        if form.is_valid():
            order = customer.order_set.create(entree=form.cleaned_data['entree'], side=form.cleaned_data['side'])
            if order.entree == 'HAM':
                price += 5
            elif order.entree == 'CHZ':
                price += 6
            elif order.entree == 'TAC':
                price += 3
            elif order.entree == 'FSH':
                price += 8
            else:
                price += 0
            if order.side == 'FRI':
                price += 3
            elif order.side == 'SAL':
                price += 2
            elif order.side == 'BNS':
                price += 3
            elif order.side == 'ORG':
                price += 5
            else:
                price += 0
            order.price = price
            order.save()
            return HttpResponseRedirect('/bacon/' + str(customer.id) + '/orders/')
    else:
        form = OrderAgainForm()
    return(render(request, 'bacon/order_again.html', {'form': form, 'customer': customer}))


