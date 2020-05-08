from django import forms
from django.forms import ModelForm

class OrderForm(forms.Form):
    first_name = forms.CharField(label="Customer First Name", max_length=50)
    last_name = forms.CharField(label="Customer Last Name", max_length=50)
    favorite = forms.CharField(label="Type your favorite food", max_length=50)
    entree = forms.ChoiceField(label="Select Entree",
                               choices=[("NA", "NONE"),
                                        ("HAM", "Hamburger"),
                                        ("CHZ", "Cheeseburger"),
                                        ("TAC", "Taco"),
                                        ("FSH", "Fish Sandwich")])
    side = forms.ChoiceField(label="Select Side",
                             choices=[('NA', 'NONE'),
                                     ('FRI', 'Fries'),
                                     ('BNS', 'Beans'),
                                     ('SAL', 'Salad'),
                                     ('ORG', 'Organs')])

class OrderAgainForm(forms.Form):
    entree = forms.ChoiceField(label="Select Entree",
                               choices=[("NA", "NONE"),
                                        ("HAM", "Hamburger"),
                                        ("CHZ", "Cheeseburger"),
                                        ("TAC", "Taco"),
                                        ("FSH", "Fish Sandwich")])
    side = forms.ChoiceField(label="Select Side",
                             choices=[('NA', 'NONE'),
                                      ('FRI', 'Fries'),
                                      ('BNS', 'Beans'),
                                      ('SAL', 'Salad'),
                                      ('ORG', 'Organs')])