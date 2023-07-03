from django import forms


class CreateOrderForm(forms.Form):
    delivery_adress = forms.CharField(
        required=True,
        widget =forms.Textarea
    )
