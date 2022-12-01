from ckeditor.widgets import CKEditorWidget
from django import forms

from history.models import History


class HistoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre de tu historia",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "history-name",
                "placeholder": "Nombre de tu historia",
                "required": "True",
            }
        ),
    )

    code = forms.IntegerField(
        label="# Publicacion",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "history-code",
                "placeholder": "# Publicacion",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Historia:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = History
        fields = ["name", "code", "description", "image"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Ingrese su comentario...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )
