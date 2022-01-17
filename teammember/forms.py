
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
        #Adding Placeholders for the form fields 
        self.fields['firstname'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FirstName'}))
        self.fields['lastname'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'LastName'}))
        self.fields['email'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
        self.fields['phone'] = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
        #Removing labels for the form 
        self.fields['firstname'].label ,self.fields['lastname'].label , self.fields['email'].label,self.fields['phone'].label = "","","",""
    # To remove - from the phone number while storing in the database
    def clean_phone(self):
        data=self.cleaned_data['phone'] 
        data=data.replace("-","")
        return data

        

      
