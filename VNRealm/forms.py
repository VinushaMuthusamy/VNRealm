# forms.py
from django import forms
from .models import PlayedList, VisualNovel
from .models import UserProfile

class PlayedListForm(forms.ModelForm):
    vn = forms.ModelChoiceField(
        queryset=VisualNovel.objects.all(),
        empty_label="Select a Visual Novel"
    )

    # metadata definition
    class Meta:
        model = PlayedList
        #user picks which VN to mark as played
        fields = ['vn']



class UserProfileForm(forms.ModelForm):
    #metadata definition
    class Meta:
        model = UserProfile
        #including profile_pic
        fields = ['profile_pic']