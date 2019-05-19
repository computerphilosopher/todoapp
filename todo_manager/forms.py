from django import forms
from django.contrib.admin import widgets   
from .models import Task 

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', ]

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget = widgets.AdminDateWidget()

'''
class TaskForm(forms.Form):

    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateTimeField(widget=)
        '''
