from django import forms
from .models import ReqSite


class ReqSiteForm(forms.ModelForm):
    class Meta:
        model = ReqSite
        fields = ['name', 'url']