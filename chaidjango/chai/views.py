from django.shortcuts import render
from .models import ChaiVarity, Store
from django.shortcuts import get_object_or_404, redirect
from .forms import ChaiVarityForm, AddChaiForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()

    return render(request, 'chai/all_chai.html', {"chais": chais})

def all_languages(request):
    return render(request, 'chai/all_lang.html')


def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)

    return render(request, 'chai/chai_detail.html', {"chai": chai})


def chai_store_view(request):
    stores = None

    if request.method == "POST":
        form = ChaiVarityForm(request.POST)

        if form.is_valid():
           chai_variety = form.cleaned_data['chai_varity']


           stores = Store.objects.filter(chai_varieties=chai_variety)

    else: 
        form = ChaiVarityForm()

    return render(request, "chai/chai_stores.html", {"stores": stores, "form": form})

def add_chai(request):
    if request.method == "POST":
        form = AddChaiForm(request.POST, request.FILES)

        if form.is_valid():
             # Get the cleaned data from the form
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            pricing = form.cleaned_data['pricing']
            chai_type = form.cleaned_data['chai_type']

            # Create a ChaiVarity instance and save it
            chai = ChaiVarity(
                name=name,
                description=description,
                image=image,
                pricing=pricing,
                type=chai_type
            )

            chai.save()

            return redirect("all_chai")

    else:
        form = AddChaiForm()

    return render(request, "chai/add_chai.html", {"form": form})

def update_chai(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)

    if request.method == "POST":
        form = AddChaiForm(request.POST, request.FILES)

        if form.is_valid():
             # Get the cleaned data from the form
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            pricing = form.cleaned_data['pricing']
            chai_type = form.cleaned_data['chai_type']

            # Create a ChaiVarity instance and save it
            ChaiVarity.objects.filter(id=chai_id).update(
                name=name,
                description=description,
                pricing=pricing,
                type=chai_type
            )

            return redirect("all_chai")
    else:

        form = AddChaiForm(initial={
        'name': chai.name,
        'description': chai.description,
        'pricing': chai.pricing,
        'chai_type': chai.type,
        })
            
    return render(request, "chai/update_chai.html", {"form": form})

def delete_chai(request, chai_id):

    if request.method == "POST":
        chai = get_object_or_404(ChaiVarity, pk=chai_id)

        chai.delete()

    return redirect("all_chai")