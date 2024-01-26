from django import forms

class OrderForm(forms.Form):
    adress_id = forms.ChoiceField(widget=forms.Select)