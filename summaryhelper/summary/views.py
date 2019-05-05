from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
def getsummary(article):

    return 'summary of ' + str(article)


def view(request):

    summary1 = getsummary(article)

    return render(request,'base.html', {'summary': summary1})

def ajax_view(request, *args, **kwargs):
    
    return JsonResponse({'a':'sujafdsfasjdnfkljsadfnlksjadfksdafsdaklf'})