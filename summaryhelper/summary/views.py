from django.shortcuts import render, get_object_or_404
from summary.models import Article, Summary
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from Rake import modelmanage


#summary model 을 통해 summary를 얻는 함수입니다.
def getsummary(article):

    q = modelmanage.extractkeyword()
    summary = q.get_Keyword(article)
    summary_text = " ".join(summary)

    return 'summary of ' + summary_text  # summary model 을 통해 summary를 얻는 함수라 할수있습니다.


#database에 저장 하는 함수입니다.
def storedb(data):

    summary_text = getsummary(data) #summary model에 article을 넣어 summary된 텍스트를 얻습니다.
    article = Article() #Article 클래스를 통해 인스턴스 생성합니다.
    article.article_text = data # data는 string형식으로 article을 파라미터로 받아 article테이블의 컬럼 article_text 에 저장해줍니다.
    article.pub_date = timezone.datetime.now()  #현재 시각기준으로 article테이블안에 컬럼 pub_date컬럼에 summary를 요청하는 시각을 넣어줍니다.
    article.save() # 각 컬럼의 저장된 값을 저장해줍니다.

    summary = Summary(id=None, summary_text=summary_text, article=article)
    # summary클래스 안에있는 속성들각각에 추가해주면서 인스턴스화 시키고 각 article 마다 summary_text는 id = 1 로 정의하며 summary_text를 정의하고
    # article컬럼은  현재 article인스턴스로 연결해줌으로써 외래키로 연결됨을 볼수있습니다.
    summary.save()  # 인스턴스 추가한 속성값을 저장해줍니다.

    return summary_text # summary 된 텍스트 를 반홥해줍니다.


#test pagex
def view(request, *args, **kwargs):

    article = 'The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet.'
    summary1 = getsummary(article)
    return render(request, 'base.html', {'summary': summary1})


@csrf_exempt #article->summary로 변환하여 Jsonresponse로 반환해주는 함수.
def ajax_view(request, *args, **kwargs):

    data = request.POST.get('article') #key값 'article'의 value를 받아 data변수로 넘겨줍니다.
    summarytext = storedb(data) # storedb 함수의 리턴값은 summary된 text입니다.
    context = {'summary': summarytext} #json형식으로 응답해줘야할 변수입니다. key값은 'summary' value는 summarytext값인 변수입니다.
    return JsonResponse(context, json_dumps_params={'ensure_ascii': True}) #client 에게 summary된 텍스트를 json 형식으로 응답해줍니다.


@csrf_exempt
def eval_ajax_view(request, *args, **kwargs) :

    eval = request.POST.get('score', '') # 사용    자에게 키값'evaluate'의 value는 숫자로이뤄진 str형입니다.

    new_eval = int(eval)  # 따라서 str 형을 int 형으로 변환 시켜줍니다.

    key = Article.objects.latest('id').id  # summary테이블 안에있는 컬럼 star에 저장하기 위해선 일단 article 테이블에 마지막 text의 id값을 key값에 저장시켜주었습니다.

    article = get_object_or_404(Article, pk=key) # 그 id값으로 article 테이블안의 컬럼과 그테이블과의 외래키로 연결된 summary테이블컬럼도 불러옵니다.

    summary_star = article.summary_set.get(article=article) # 위 id값으로 불러온 article과 연결된 summary테이블의 컬럼들을 불러와 summary된 텍스트의 별점을 매길수 있도록합니다.

    summary_star.star = new_eval #아까 선언한 int형 숫자를 star변수에 넣어줍니다.

    summary_star.save()  #star컬럼에 넣어준 숫자를 저장합니다.

    context = {'score': eval} # context 변수로 key는 'evaluate'라하고 string형 변수를 client 에게 넘겨줍니다.
    return JsonResponse(context, json_dumps_params={'ensure_ascii' : True}) #key와 value로 이뤄진 json형식을 client에게 반환합니다.