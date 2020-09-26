from django import forms
from tool.models import Commit

class CommitForm(forms.ModelForm):
    """ CommitForm describes the interface to input commit message
        in a text box.
    """
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Enter text here."
        }))

    # fields only includes 'body' from the class Commit
    # inside models.py to save commit message.
    class Meta:
        model = Commit
        fields = ('body',)
