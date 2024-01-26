from django import forms
from .models import ProductsCommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductsCommentModel
        fields = ["comment_text"]