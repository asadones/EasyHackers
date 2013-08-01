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

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Titre de l\'offre',
    )
    name_company = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Nom de l\'entreprise',
    )
    num_employee = forms.ChoiceField(
        choices=_employee_choices,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label=u'Nombre d\'employés',
    )
    localisation = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Localisation de l\'offre',
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label=u'Description de l\'offre',
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Email',
    )

    nom_contact = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Nom',
    )
    prenom_contact = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label=u'Prénom',
    )
    phone_contact = forms.RegexField(
        regex=_phone_re,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Numéro de téléphone',
    )
