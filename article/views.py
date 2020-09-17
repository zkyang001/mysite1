from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article

# Create your views here.

def article_list(request):
	articles = Article.objects.all()
	article_list = {}
	article_list['list'] = articles
	return render_to_response('article_list.html', article_list) 


def article_detail(request, id):
	article = get_object_or_404(Article, pk=id)
	content = {}
	content["each"] = article
	return render_to_response("article_detail.html", content)