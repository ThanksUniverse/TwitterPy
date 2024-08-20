from django import forms  
from tweets.models import Tweet  
from tweets.models import UserProfile

class TweetForm(forms.ModelForm):  
    class Meta:  
        model = Tweet  
        fields = ['content', 'image'] 

    image = forms.ImageField(required=False)  

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            max_size = 5 * 1024 * 1024  # 5MB
            if image.size > max_size:
                raise forms.ValidationError("A imagem não pode exceder 5MB.")
        
        return image

from datetime import date
from django.core.exceptions import ValidationError

class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False,
        label="Data de Nascimento"
    )

    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'website', 'birth_date', 'profile_image']

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date:
            if birth_date > date.today():
                raise ValidationError("A data de nascimento não pode ser no futuro.")
            if birth_date < date(1900, 1, 1):
                raise ValidationError("A data de nascimento parece inválida. Por favor, insira uma data realista.")
        return birth_date

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website:
            if not website.startswith(('http://', 'https://')):
                raise ValidationError("O website deve começar com 'http://' ou 'https://'.")
        return website

    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image')
        if image:
            max_size = 2 * 1024 * 1024  # 2MB
            if image.size > max_size:
                raise forms.ValidationError("A imagem não pode exceder 2MB.")
        return image