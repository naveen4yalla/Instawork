
from logging import PlaceHolder
from django import forms
from .models import People

class PostForm(forms.ModelForm):
    class Meta:
        model=People
        fields ="__all__"
        #fields = ["firstname","lastname","email","phone","choice"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["choice"]=forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=People.role)
        #Adding Placeholders
        self.fields['firstname'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FirstName','label':""}))
        self.fields['lastname'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
        self.fields['email'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
        self.fields['phone'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
        #Removing labels for the form 
        self.fields['firstname'].label ,self.fields['lastname'].label , self.fields['email'].label,self.fields['phone'].label = "","","",""
        

      