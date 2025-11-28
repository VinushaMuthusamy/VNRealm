# forms.py
from django import forms
from .models import PlayedList, VisualNovel
from .models import UserProfile

class PlayedListForm(forms.ModelForm):
    vn = forms.ModelChoiceField(
        queryset=VisualNovel.objects.all(),
        empty_label="Select a Visual Novel"
    )
    class Meta:
        model = PlayedList
        fields = ['vn']  # Let the user pick which VN to mark as played



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']  # include profile_pic