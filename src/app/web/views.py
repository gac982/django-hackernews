from django.shortcuts import render, redirect, reverse
from app.api.models import News
from app.web.forms import NewsForms

# Create your views here.
def home(request):
	return render(request, 'pages/list.html', {})

def add_news(request):
	mi_form = NewsForms()
	# validamos el formulario
	if request.method == 'POST':
		mi_form = NewsForms(request.POST)
		# en caso contario muestro los errores
		if mi_form.is_valid():
			# si todo es valido guardo
			mi_new_news = News()
			# mi_new_news.title = request.POST['title']
			mi_new_news.title = mi_form.cleaned_data.get('title')
			# mi_new_news.url = request.POST['url']
			mi_new_news.url = mi_form.cleaned_data.get('url')
			mi_new_news.save()
			# redirecciono a Home
			return redirect(reverse('home'))

	return render(request, 'pages/add-news.html', {
		'news_form': mi_form
		})