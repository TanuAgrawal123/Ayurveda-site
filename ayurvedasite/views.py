from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment, Symptoms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home_page(request):
	comments=Comment.objects.all().order_by('-id')
	return render(request, 'ayurvedasite/home.html', {'comments':comments})

def intro_page(request):
	return render(request, 'ayurvedasite/intro.html',{})

	
def add_comment(request):
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.save()
			return redirect('ayurvedasite:home_page')
	else:
		form = CommentForm()
		return render(request, 'ayurvedasite/add_comment.html', {'form': form})

def symptoms(request):
	symptoms_list =Symptoms.objects.all().order_by('id')
	paginator = Paginator(symptoms_list,2,allow_empty_first_page=False)
	page=request.GET.get('page',1)
	sym=paginator.page(page)
	print("hi")
	return render(request, 'ayurvedasite/symptoms.html', {'sym': sym})



