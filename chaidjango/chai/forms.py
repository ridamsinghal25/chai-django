from django import forms
from .models import ChaiVarity

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select Chai Variety")

class AddChaiForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            'placeholder': 'Enter chai name'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            'placeholder': 'Enter description',
            'rows': 4
        })
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full text-gray-700'
        }),
        required=False
    )
    pricing = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500',
            'placeholder': 'Enter price'
        })
    )
    chai_type = forms.ChoiceField(
        choices=ChaiVarity.CHAI_TYPE_CHOICE,
        widget=forms.Select(attrs={
            'class': 'w-full border rounded px-3 py-2 focus:outline-none focus:ring focus:border-blue-500'
        })
    )