from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Users, Messages

j = []
for i in range(70):
    j.append(1945+i)


class CreateUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('name', 'sname', 'birthday')
        widgets = {'birthday': SelectDateWidget(years=j)}


class CreateMessage(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=Users.objects.all(), empty_label=None)

    class Meta:
        model = Messages
        fields = ('message', 'user')
