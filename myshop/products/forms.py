from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(required="True", error_messages={"required": "You forgot to add your name."})
    email = forms.EmailField()