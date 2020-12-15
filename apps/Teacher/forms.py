from django import forms


class TeacherTaskFilter(forms.Form):
    verified = forms.BooleanField(label="Проверенные", required=False, widget=forms.CheckboxInput)
    not_verified = forms.BooleanField(label="Не проверенные", required=False, widget=forms.CheckboxInput)
