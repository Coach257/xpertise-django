from django.shortcuts import render
from django.http import HttpResponse
from scholarly import scholarly
import json
# Create your views here.

def index(request):
    return HttpResponse("Xpertise Scholar")

# 搜索作者，返回作者的个人信息
def search_author(request):
    author_name = request.POST['author_name']
    #author_name = 'Mark'
    author = next(scholarly.search_author(author_name))
    res = {'affiliation': author.affiliation,
           #'citedby': author.citedby,
           'email': author.email,
           #'filled': author.filled,
           'id': author.id,
           'interests': author.interests,
           'name': author.name,
           'url_picture': author.url_picture}
    return HttpResponse(json.dumps(res), content_type="application/json")

def search_paper(request):
    paper_name = request.POST['paper_name'] # 文献名
    #paper_name = 'Li Buyu'
    paper=next(scholarly.search_pubs(paper_name))
    content = {
        'url':paper.bib['url'],
        'venue': paper.bib['venue'],
        'abstract': paper.bib['abstract']}
    return HttpResponse(json.dumps(content), content_type="application/json")