from django import forms  
from tweets.models import Tweet  
from tweets.models import UserProfile

class TweetForm(forms.ModelForm):  
    class Meta:  
        model = Tweet  
        fields = ['content']  # Inclua apenas o campo 'content'

class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'website', 'birth_date', 'profile_image']

    def clean_profile_image(self):
        image = self.cleaned_data.get('profile_image')

        if image:
            max_size = 2 * 1024 * 1024  # 2MB
            if image.size > max_size:
                raise forms.ValidationError("A imagem não pode exceder 2MB.")
        
        return image
