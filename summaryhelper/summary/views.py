from django.shortcuts import render, get_object_or_404
from summary.models import Article, Summary
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.utils import timezone
def getsummary(article):

    # write down models method()

    return 'summary of ' + str(article)

def getarticle(*args):

    return str(args)


def storedb(*args, **kwargs):

    summary_text = getsummary(args)
    article = Article()
    article.article_text = args
    article.pub_date = timezone.datetime.now()
    article.save()

    summary = Summary(id=1, summary_text=summary_text, article=article)
    summary.save()

    return summary_text


#test page
def view(request, *args, **kwargs):

    article = 'The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet.'
    summary1 = getsummary(article)
    return render(request,'base.html', {'summary': summary1})


@csrf_exempt
def ajax_view(request, *args, **kwargs):

    data = request.POST.get('article')

    summarytext = storedb(data)
    context = {'summary': summarytext}
    return JsonResponse(context, json_dumps_params={'ensure_ascii': True})

@csrf_exempt
def eval_ajax_view(request, *args, **kwargs) :

    eval = request.POST.get('evaluate', None)

    key = Article.objects.latest('id').id
    article = get_object_or_404(Article, pk=key)

    summary_star = article.summary_set.get(pk=1)

    new_eval = int(eval)

    summary_star.star += new_eval

    summary_star.save()

    context = {'evaluate': eval}
    return JsonResponse(context, json_dumps_params={'ensure_ascii' : True})