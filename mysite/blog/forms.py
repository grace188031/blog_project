from django import forms
from blog.models import Post,Comments
from django_quill.forms import QuillFormField


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','title','text', 'image')
        text=QuillFormField()

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # 'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

        }
    

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('author','text')


        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }



