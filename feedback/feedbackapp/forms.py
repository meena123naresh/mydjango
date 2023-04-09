from django import forms
class feedbackform(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
        attrs={'placeholder':'Your Name','class':'form-control'}))
    tutorname=forms.CharField(
        label="Enter tutor Name",
            widget=forms.TextInput(
        attrs={'placeholder':'tutor Name','class':'form-control'}))
    feedback12=forms.CharField(
        label="enter feedback",widget=forms.Textarea(
        attrs={'rows':5,'cols':20,'class':'form-control'}))
