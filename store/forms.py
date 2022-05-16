from django import forms
from .models import Application
from .models import Order


class ApplicationForms(forms.ModelForm):
    class Meta:
        model = Application
        fields = {'name', 'email', 'number', 'message'}


class OrderForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Имя')
    e_mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}), label='E-mail')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Телефон')
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Страна')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Город')
    street = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Улица')
    house = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Дом')
    flat = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Квартира')

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'country', 'city', 'street', 'house', 'flat']
