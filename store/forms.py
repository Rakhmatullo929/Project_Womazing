from django import forms
from .models import Application, Feedback, CartItem
from .models import Order, COLOR_CHOICES, SIZE_CHOICES


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


class RateForm(forms.ModelForm):
    size = forms.ChoiceField(choices=SIZE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio_select '}),
                             label='Выберите размер')
    color = forms.ChoiceField(choices=COLOR_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio_selects'}), label='Выберите цвет')

    class Meta:
        model = CartItem
        fields = ('size', 'color')


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'client_name', 'client_email', 'client_number'}
