from django.core.exceptions import ValidationError

from .models import *
from django import forms


# class AddPostForm(forms.Form):
    # nik_name = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # slug = forms.SlugField(max_length=255, label="URL")
    # about = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    # is_published = forms.BooleanField(label="Публикация", required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Visitor
        # fields = '__all__'
        fields = ['nik_name', 'slug', 'about', 'photo', 'is_published', 'cat']  # No photo
        widgets = {
            'nik_name': forms.TextInput(attrs={'class': 'form-input'}),
            'about': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_nik_name(self):
        nik_name = self.cleaned_data['nik_name']
        if len(nik_name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return nik_name






