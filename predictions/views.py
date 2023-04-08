from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SymptomsForm
from django.urls import reverse
from django.contrib import messages
from .utils import DecisionTree, randomforest, NaiveBayes


# Create your views here.
@login_required()
def search(request):

    if request.method == 'POST':
        form = SymptomsForm(request.POST)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        if form.is_valid():
            symptom1 = form.get_info()[0]
            symptom2 = form.get_info()[1]
            symptom3 = form.get_info()[2]
            symptom4 = form.get_info()[3]
            symptom5 = form.get_info()[4]

            return redirect(reverse('predictions:results') +
                         f'?symptom1={symptom1}&symptom2={symptom2}&symptom3={symptom3}&symptom4={symptom4}&symptom5={symptom5}')

    else:
        form = SymptomsForm()
        
        context = {
            'form': form
            
        }

        return render(request, 'predictions/search.html', context)


@login_required()
def results(request):

    try:
        symptom1 = request.GET['symptom1']
        symptom2 = request.GET['symptom2']
        symptom3 = request.GET['symptom3']
        symptom4 = request.GET['symptom4']
        symptom5 = request.GET['symptom5']
    except:
        messages.error(request, 'Sorry something happened, try again')
        return redirect(reverse('predictions:search'))

    # Call the functions
    test1 = DecisionTree(symptom1, symptom2, symptom3, symptom4, symptom5)
    test2 = randomforest(symptom1, symptom2, symptom3, symptom4, symptom5)
    test3 = NaiveBayes(symptom1, symptom2, symptom3, symptom4, symptom5)

    context = {
        'test1': test1,
        'test2': test2,
        'test3': test3
    }

    return render(request, 'predictions/results.html', context)