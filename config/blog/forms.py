from django import forms
from blog import models


class UploadImagesForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = models.UploadedImage
        fields = ('id', 'image')


class PostCreateForm(forms.Form):
    name = forms.CharField(max_length=30, label='Nomi')
    description = forms.CharField(widget=forms.Textarea, label='Tavsif')
    # image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Rasm')
    category = forms.ModelChoiceField(label='Kategoriya', queryset=models.Category.objects.all())
    region = forms.ModelChoiceField(label='Hudud', queryset=models.Region.objects.all())
