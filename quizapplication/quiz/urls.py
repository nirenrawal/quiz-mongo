from django.urls import path
from . import views


app_name = 'quiz'

urlpatterns = [
    path('create_quiz_category/', views.create_quiz_category, name='create_quiz_category'),
    path('add_quiz_question/', views.add_quiz_question, name='add_quiz_question'),
    path('show_quiz_question/', views.show_quiz_question, name='show_quiz_question'),
    path('quiz_index/', views.quiz_index, name='quiz_index'),
    path('delete_quiz_question/<int:question_id>/', views.delete_quiz_question, name='delete_quiz_question'),
    path('update_quiz_category/<int:category_id>/', views.update_quiz_category, name='update_quiz_category'),
    path('show_quiz_category/', views.show_quiz_category, name='show_quiz_category'),
    path('delete_quiz_category/<int:category_id>', views.delete_quiz_category, name='delete_quiz_category'),
    path('add_answer_to_questions/<int:question_id>/', views.add_answer_to_questions, name='add_answer_to_questions'),
    
    
    path('view_quiz/<int:category_id>/', views.view_quiz, name='view_quiz'), #problem
    path('submit_quiz/<int:category_id>/', views.submit_quiz, name='submit_quiz'),
    path('quiz_result/<int:category_id>/<int:user_score_id>/', views.quiz_result, name='quiz_result'),

    
    
]

