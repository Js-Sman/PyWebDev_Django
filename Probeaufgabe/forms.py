from django import forms
import datetime


class ProbeaufgabeForm(forms.Form):

    name = forms.CharField(label='Name', max_length=80)
    semester = forms.IntegerField(label='Semester')
    start_date = forms.DateField(label='Start')
    average = forms.DecimalField(label='Average', decimal_places=1)
