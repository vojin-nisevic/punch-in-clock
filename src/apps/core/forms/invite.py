from django import forms


class InviteForm(forms.Form):
    recipient = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email recipient'}))
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
