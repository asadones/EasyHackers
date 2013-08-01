from django import forms


class OfferForm(forms.Form):
    title = forms.CharField(required=True)
    name_company = forms.CharField(required=True)
    employee_choices = ["1 à 5", "6 à 20", "20 à 100",
                        "100 à 249", "plus de 250"]
    num_employee = forms.MultipleChoiceField(
        choices=employee_choices,
        required=True,
    )
    localisation = forms.CharField(required=True)
    description = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    nom_contact = forms.CharField(required=True)
    prenom_contact = forms.CharField(required=True)
    phone_re = r'^0[1-6]{1}(([0-9]{2}){4})|((\s[0-9]{2}){4})|((-[0-9]{2}){4})$'
    phone_contact = forms.RegexField(regex=phone_re, required=True)

