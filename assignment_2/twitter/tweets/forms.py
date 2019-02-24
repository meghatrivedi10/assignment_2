from django import forms
from .models import Tweetlist


class TweeetForm(forms.ModelForm):
    tweet = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'class' : 'form-control tweet-box'}) )
    class Meta:
        model = Tweetlist
        fields = ('tweet',)
