# forms.py
from django import forms
from .models import PlayedList, VisualNovel
from .models import UserProfile

#form for played_list
#default dropdownlabel set and all vns included in the set
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


#form for profile picture uploading
class UserProfileForm(forms.ModelForm):
    #metadata definition
    class Meta:
        model = UserProfile
        #including profile_pic
        fields = ['profile_pic']