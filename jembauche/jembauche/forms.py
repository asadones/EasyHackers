# -*- coding: utf-8 -*-
from django import forms


class OfferForm(forms.Form):

    _employee_choices = (
        (u'1', u'1 à 5'),
        (u'2', u'6 à 20'),
        (u'3', u'20 à 100'),
        (u'4', u'100 à 249'),
        (u'5', u'plus de 250'),
    )
    _phone_re = r'^0[1-6]{1}(([0-9]{2}){4})|((\s[0-9]{2}){4})|((-[0-9]{2}){4})$'

    title = forms.CharField(required=True)
    name_company = forms.CharField(required=True)
    num_employee = forms.MultipleChoiceField(
        choices=_employee_choices,
        required=True,
    )
    localisation = forms.CharField(required=True)
    description = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    nom_contact = forms.CharField(required=True)
    prenom_contact = forms.CharField(required=True)
    phone_contact = forms.RegexField(regex=_phone_re, required=True)

