from django import forms


class AddForm(forms.Form):

    def __init__(self, fdata, *args, **kwargs):
        print("domici-------------",fdata)
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['domicilio'].widget = forms.TextInput(attrs={'value':fdata,"class":"form-control",
                "id":"domicilio",})

    cantidad  = forms.IntegerField(label="Cantidad",widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "id":"cantidad",
            }))

    domicilio = forms.CharField(label="Domicilio ",widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"domicilio",
            }))


    observacion = forms.CharField(required=False,label="Observacion",widget=forms.TextInput(attrs={
                "class":"form-control",
                "id":"observacion",
            }))


    def clean(self):
        data = self.cleaned_data
        cantidad = data.get('cantidad')
        if cantidad <= 0 or cantidad >= 11:
            raise forms.ValidationError("debes pedir minimo 1 y no mas de 10")


