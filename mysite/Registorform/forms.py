from django import forms

class ReviewForm(forms.Form):
    user_name=forms.CharField(label='your Name',max_length=20)