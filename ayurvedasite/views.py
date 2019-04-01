from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment, Symptoms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request):
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.save()
			form=CommentForm()
	else:
		form = CommentForm()
	comments=Comment.objects.all().order_by('-id')
	return render(request, 'ayurvedasite/home.html', {'comments':comments, 'form':form})

def intro_page(request):
	return render(request, 'ayurvedasite/intro.html',{})

	
def symptoms(request):
	symptoms_list =Symptoms.objects.all().order_by('id')
	paginator = Paginator(symptoms_list,2,allow_empty_first_page=False)
	page=request.GET.get('page',1)
	sym=paginator.page(page)
	return render(request, 'ayurvedasite/symptoms.html', {'sym': sym})
	





