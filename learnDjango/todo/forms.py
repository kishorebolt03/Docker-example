from django import forms
from .models import Todo

class addTodoForm(forms.Form):
    text = forms.CharField(max_length=40, 
    widget = forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Task eg: Finish assignment'}
    ))

class newTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text' : forms.TextInput(
                attrs={'class' : 'form-control', 'placeholder' : 'Task eg: Finish assignment'}
            )
        }