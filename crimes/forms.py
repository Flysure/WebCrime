from django import forms

class crimeForm(forms.Form):
    date_reported_beg = forms.DateField(label='Date Beginning')
    date_reported_end = forms.DateField(label='Date Ending')
    radius = forms.IntegerField(label='Radius')
    type = forms.ChoiceField(choices=[('01110', 'Murder')])
