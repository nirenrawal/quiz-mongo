from djongo import models
from django.contrib.auth.models import User

class QuizCategory(models.Model):
    _id = models.BigAutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration in Seconds", default=1)
    
    class Meta:
        verbose_name_plural = "quiz catogeries"
        
    
    def __str__(self):
        return self.name
    
    def get_question(self):
        return self.question_set.all()


class Question(models.Model):
    _id = models.BigAutoField(primary_key=True, blank=True)
    content = models.CharField(max_length=255)
    quiz_category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
   
    
    def __str__(self):
        return f"{self.content} ----------------------------- {self.quiz_category}"
    
    def get_answers(self):
        return self.answer_set.all()
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            num_existing_questions = Question.objects.filter(quiz_category=self.quiz_category).count()
            if num_existing_questions >= self.quiz_category.number_of_questions:
                raise ValueError(f"You cannot create more questions then {self.quiz_category.number_of_questions} questions in this category.")
        super().save(*args, **kwargs)
            
    
    
class Answer(models.Model):
    _id = models.BigAutoField(primary_key=True, blank=True)
    content = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Question: {self.question.content}, answer: {self.content}, Correct Answer: {self.correct_answer}"
    

class UserScore(models.Model):
    _id = models.BigAutoField(primary_key=True, blank=True)
    quiz_category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.user} - {self.quiz_category}"
    
    