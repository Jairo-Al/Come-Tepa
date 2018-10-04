from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electronico",widget=forms.EmailInput(
            attrs={
                "class":"form-control ",
                "id":"",
            }))

    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "id":"contrasena",
            }))

User = get_user_model()

class RegisterForm(forms.Form):
    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"nombre",
            }))

    telefono   = forms.IntegerField(label="Telefono",widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "id":"telefono",
            }))

    domicilio = forms.CharField(label="Domicilio",widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"domicilio",
            }))


    email    = forms.EmailField(widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "id":"email",

            }))
    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "id":"contrasena",
                "label":"Contraseña"
            }))
    contrasena2 = forms.CharField(label="Confirma Contraseña",widget=forms.PasswordInput(attrs={
                "class":"form-control",
                "id":"contrasena2",
            }))




    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Correo ya existe")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('contrasena')
        password2 = data.get('contrasena2')
        if password2 != password:
            raise forms.ValidationError("Contraseñas deben ser iguales")
        nombre = data.get('nombre')
        if len(nombre) <= 6:
            raise forms.ValidationError("Nombre debe ser mayor a 6 characteres")
        return data

