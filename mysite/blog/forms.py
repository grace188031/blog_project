from django import forms
from blog.models import Post,Comments
from django_ckeditor_5.widgets import CKEditor5Widget


class PostForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["text"].required = False
    class Meta:
        model = Post
        fields = ('author','title','text', 'image')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }

    

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('author','text')


        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }



