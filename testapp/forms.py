from django import forms
from testapp.models import Movie



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels ={'rdate': 'Released Date(yyyy-mm-dd)','mrating': 'Movie Rating'}
        