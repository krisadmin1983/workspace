from django import forms
from .models import Message, CommunityMessage

class MessageForm(forms.ModelForm):
    message = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'placeholder': 'What\'s on your mind?'}))

    class Meta:
        model = Message
        fields = ('message',)

class CommunityMessageForm(forms.ModelForm):
    message = forms.CharField(max_length=140, widget=forms.TextInput(attrs={'placeholder': 'Share with the community'}))

    class Meta:
        model = CommunityMessage
        fields = ('message',)
