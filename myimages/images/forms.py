from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your image name'}))

    class Meta:
        model = Image
        fields = ['title', 'photo']
