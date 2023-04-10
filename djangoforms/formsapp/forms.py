from django import forms
class contactform(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(attrs={'placeholder':'Your name','class':'form-control'})
    )
    email=forms.CharField(label="Enter email",
                          widget=forms.EmailInput(attrs={'placeholder':'your email','class':'form-control'}))
    phone=forms.IntegerField(label='Enter your mobile number',
                             widget=forms.NumberInput(attrs={'placeholder':'your number','class':'form-control'}))
    city=forms.CharField(
        label="Enter your city",
        widget=forms.TextInput(attrs={'placeholder':'Your city','class':'form-control'}))