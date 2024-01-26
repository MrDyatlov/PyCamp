from django import forms
from .models import AdressModel

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username:", required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, label="Password", required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control form-control-lg"})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control form-control-lg"})


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username", required=True)
    email = forms.CharField(max_length=150, label="Email", required=True)
    password = forms.CharField(max_length=100, label="Password", required=True)
    confirm = forms.CharField(max_length=100, label="Password Confirm", required=True)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control form-control-lg"})
        self.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control form-control-lg"})
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"class": "form-control form-control-lg"})
        self.fields["confirm"].widget = forms.PasswordInput(
            attrs={"class": "form-control form-control-lg"})

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password != confirm:
            raise forms.ValidationError("Password's didn't match!")

        values = {"username": username, "email": email, "password": password, "confirm": confirm}
        return values


class AdressForm(forms.ModelForm):
    class Meta:
        model = AdressModel
        fields = ["adress_title", "adress_city", "adress_district", "adress_neighborhood", "adress_description"]
        
    def __init__(self, *args, **kwargs):
        super(AdressForm, self).__init__(*args, **kwargs)
        self.fields["adress_title"].widget = forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Home, Office vs."})
        self.fields["adress_city"].widget = forms.Textarea(
            attrs={"class": "form-control"})
        self.fields["adress_district"].widget = forms.TextInput(
            attrs={"class": "form-control"})
        self.fields["adress_neighborhood"].widget = forms.Textarea(
            attrs={"class": "form-control"})
        self.fields["adress_description"].widget = forms.TextInput(
            attrs={"class": "form-control", "rows": 4, "style": "max-height: 150px;"})