from django import forms
from .models import RecipeItem

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

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ('name', 'image', 'prep_time', 'cook_time', 'servings', 'ingredients',
            'directions', 'cuisine',)
    

class MenuForm(forms.Form):
    name = forms.CharField(label='Menu Title', max_length=100)
    starter = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Starter'), required=False)
    first = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='First'), required=False)
    second = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Second'), required=False)
    side1 = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Side'), required=False)
    side2 = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Side'), required=False)
    side3 = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Side'), required=False)
    dessert = forms.ModelChoiceField(queryset=RecipeItem.objects.filter(course='Dessert'), required=False)

