from django.shortcuts import render, redirect, get_object_or_404
from .form import QuizCategoryForm, QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Question, QuizCategory, Answer, UserScore
from django.contrib import messages
from django.forms import inlineformset_factory





# @login_required
# def quiz_index(request):
#     quiz_categories = QuizCategory.objects.using('quiz').all()
    
#     items = quiz_categories.get({})
#     quiz_categories = list()
    
#     for item in items:
#         id = item.pop('_id')
#         item['id'] = id
#         quiz_categories.append(item)
#     return render(request, "quiz/quiz_index.html", {'quiz_categories':quiz_categories})
@login_required
def quiz_index(request):
    quiz_categories = QuizCategory.objects.using('quiz').all()
    transformed_categories = []
    for category in quiz_categories:
        category_data = {
            'id': str(category._id),  # Convert ObjectId to string
            'name': category.name,
            # Add other category attributes as needed
        }
        transformed_categories.append(category_data)

    return render(request, "quiz/quiz_index.html", {'quiz_categories': transformed_categories})

""" This function creates quiz category """

@login_required
def create_quiz_category(request):
    if request.method == 'POST':
        form = QuizCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            if not QuizCategory.objects.filter(name=category_name).exists():
                form.save()
                messages.success(request, "Your Quiz Category Has Been Created.")
                return redirect('quiz:quiz_index')
            else:
                messages.error(request, "The Quiz Category Already Exists.")
        else:
            messages.error(request, "Your Form Data Is Invalid.")
    else:
        form = QuizCategoryForm()
    return render(request, 'quiz/create_quiz_category.html', {'form': form})






""" This function adds quizes in database """
@login_required
def add_quiz_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = QuestionForm()
                messages.success(request, "Your quiz question has been added successfully.")
            except ValueError as e:
                error_msg = str(e)
                messages.error(request, error_msg)
    else:
        form = QuestionForm()
    return render(request, "quiz/add_quiz_question.html", {'form':form}) 


def show_quiz_question(request):
    questions = Question.objects.all()
    return render(request, "quiz/show_quiz_question.html", {'questions':questions})


""" This function deletes the quiz questions """
@login_required
def delete_quiz_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        question.delete()
        messages.success(request, "The quiz question has been deleted successfully.")
    except Question.DoesNotExist:
        messages.error(request, "The quiz question does not exist.")
    return redirect('quiz:show_quiz_question')


@login_required
def delete_quiz_category(request, category_id):
    try:
        category = QuizCategory.objects.get(id=category_id)
        category.delete()
        messages.success(request, "The quiz category has been deleted successfully.")
    except Question.DoesNotExist:
        messages.error(request, "The quiz category does not exist.")
    return redirect('quiz:show_quiz_category')


@login_required
def show_quiz_category(request):
    quiz_categories = QuizCategory.objects.all()
    return render(request, "quiz/show_quiz_category.html", {'quiz_categories':quiz_categories})

    
@login_required
def update_quiz_category(request, category_id):
    quiz_category = get_object_or_404(QuizCategory, id=category_id)
    
    if request.method == 'POST':
        form = QuizCategoryForm(request.POST, instance=quiz_category)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            if not QuizCategory.objects.filter(name=category_name).exclude(id=category_id).exists():
                form.save()
                messages.success(request, "The quiz category has been updated successfully.")
                return redirect('quiz:show_quiz_category')
            else:
                messages.error(request, "The quiz category already exists.")
        else:
            messages.error(request, "The form data is invalid.")
    else:
        initial_val = {
            'name': quiz_category.name,
            'description': quiz_category.description,
            'number_of_questions': quiz_category.number_of_questions,
            'time': quiz_category.time,
        }
        form = QuizCategoryForm(instance=quiz_category, initial=initial_val)
    return render(request, "quiz/update_quiz_category.html", {'form': form})



@login_required
def add_answer_to_questions(request, question_id):
    question = Question.objects.get(id=question_id)
    question_form_set = inlineformset_factory(Question, Answer, fields=('content', 'correct_answer', 'question'), extra=4, max_num=4)
    if request.method == 'POST':
        form = question_form_set(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "Added Successfully.")
            return redirect('quiz:show_quiz_question')
    else:
        form = question_form_set(instance=question)
    return render(request, "quiz/add_answer_to_questions.html", {'form':form, 'question':question})



@login_required
def view_quiz(request, category_id):
    try:
        category = get_object_or_404(QuizCategory, id=category_id)
        questions = category.get_question()
        return render(request, "quiz/view_quiz.html", {'category': category, 'questions': questions})
    except QuizCategory.DoesNotExist:
        messages.error(request, "Quiz category does not exist.")
        return redirect('quiz:quiz_categories')


@login_required
def submit_quiz(request, category_id):
    if request.method == 'POST':
        try:
            category = get_object_or_404(QuizCategory, id=category_id)
            questions = category.get_question()
            score = 0
            total_questions = 0

            for question in questions:
                total_questions += 1
                selected_answer_id = request.POST.get(f'question_{question.id}')
                try:
                    selected_answer = get_object_or_404(Answer, id=selected_answer_id)
                except Answer.DoesNotExist:
                    error_message = "Selected answer does not exist."
                    return render(request, 'error.html', {'error_message': error_message})

                if selected_answer.correct_answer:
                    score += 1

            percentage = (score / total_questions) * 100
            user_score = UserScore.objects.create(quiz_category=category, user=request.user, score=score)

            context = {
                'category': category,
                'category_id': category_id,
                'questions': questions,
                'user_score_id': user_score.id,
                'percentage': percentage,
                'duration': category.time,
            }
            return redirect('quiz:quiz_result', category_id=category_id, user_score_id=user_score.id)
        except QuizCategory.DoesNotExist:
            error_message = "Quiz category does not exist."
            return render(request, 'error.html', {'error_message': error_message})
    else:
        error_message = "Invalid request method."
        return render(request, 'error.html', {'error_message': error_message})



@login_required
def quiz_result(request, category_id, user_score_id):
    try:
        category = get_object_or_404(QuizCategory, id=category_id)
        user_score = get_object_or_404(UserScore, id=user_score_id, quiz_category=category, user=request.user)
        total_questions = category.number_of_questions
        percentage = (user_score.score / total_questions) * 100

        context = {
            'category': category,
            'user_score': user_score,
            'total_questions': total_questions,
            'percentage': percentage,
        }

        return render(request, "quiz/quiz_result.html", context)
    except (QuizCategory.DoesNotExist, UserScore.DoesNotExist):
        messages.error(request, "Quiz result not found.")
        return redirect('quiz:quiz_categories')









