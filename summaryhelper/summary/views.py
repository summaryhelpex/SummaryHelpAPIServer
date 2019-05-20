from django.shortcuts import render, get_object_or_404
from summary.models import Article, Summary
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
def getsummary(article):

    # write down models method()
    return 'summary of ' + str(article)


def storedb(request, *args, **kwargs):
    article = Article()
    summary = Summary()

    #return_summary = request
    article.article_text = args
    article.pub_date = timezone.datetime.now()
    article.save()

#    new_article = get_object_or_404(Article, pk=)
    summary.summary_text = getsummary(args)


    summary.save()

    return summary.summary_text


#test page
def view(request, *args, **kwargs):

    article = 'The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet.'
    summary1 = getsummary(article)
    return render(request,'base.html', {'summary': summary1})


@csrf_exempt
def ajax_view(request, *args, **kwargs):

#    summary = Summary()
#    if request.POST.get('evaluate') == True :
#        print(request.POST['evaluate'])
    #summary
    data = request.POST.get('article')

    #storedb(request, data)
    context = {'article': data}
    return JsonResponse(context, json_dumps_params={'ensure_ascii': True})

def eval_ajax_view(request, *args, **kwargs) :

    eval = request.POST.get('evaluate', None)
    context = {'evaluate': eval}
    return JsonResponse(context, json_dumps_params={'ensure_ascii' : True})
'''    
def ajax_view(request, *args, **kwargs):
    
    return JsonResponse({'a':'sujafdsfasjdnfkljsadfnlksjadfksdafsdaklf'})'''