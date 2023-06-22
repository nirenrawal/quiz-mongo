from django import forms
from .models import QuizCategory, Question

class QuizCategoryForm(forms.ModelForm):
    class Meta:
        model = QuizCategory
        fields = ('name', 'description', 'number_of_questions', 'time')
       

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz_category')
        widgets = {
            
        }
    
