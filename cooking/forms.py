from django import forms

COURSE_CHOICES = [
    ('Starter', 'Starter'),
    ('First', 'First'),
    ('Second', 'Second'),
    ('Side', 'Side'),
    ('Dessert', 'Dessert')
]

class RecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Title', max_length=100)
    image = forms.ImageField(required=False)
    prep_time = forms.IntegerField(label='Prep Time in Minutes')
    cook_time = forms.IntegerField(label='Cook Time in Minutes')
    servings = forms.IntegerField()
    ingredients = forms.CharField(widget=forms.Textarea)
    directions = forms.CharField(widget=forms.Textarea)
    course = forms.CharField(widget=forms.Select(choices=COURSE_CHOICES))
    cuisine = forms.CharField(max_length=30)
    