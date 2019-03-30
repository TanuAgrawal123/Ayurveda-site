from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment
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
	return render(request,'ayurvedasite/symptoms.html')





