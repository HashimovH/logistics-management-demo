from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_picture', 'color_choice', 'title', 'about']
