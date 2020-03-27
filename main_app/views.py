from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish
from .forms import WishForm

# Create your views here.


def home(request):
    wishes = Wish.objects.all()
    return render(request, 'home.html', {
        'wishes' : wishes
    })

class WishCreate(CreateView):
    model = Wish
    success_url = '/'
    fields = ['description']
    def form_valid(self, form):
        return super().form_valid(form)

def delete_wish(request, wish_id):
    Wish.objects.get(id=wish_id).delete()
    return redirect('home')

