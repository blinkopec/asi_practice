from django import forms

class EditingForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=50)
    surname = forms.CharField(label='Фамилия', max_length=50)
    # dateReport = forms.DateField(label='Дата подписания')