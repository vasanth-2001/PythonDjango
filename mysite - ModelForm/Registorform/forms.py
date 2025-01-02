from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label='your Name',max_length=20)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        lables={
            'user_name':'Your Name',
            'rating':'Your Rating',
            'review_text':'Your Feedback'
        }