import tfidfDE
from rake_nltk import Rake
from summa import keywords
import yake
class extractkeyword:
    tfidfres=[]
    def __init__(self):
        self.rakemod=Rake()

       
    def get_Keyword(self,text):
        self.rakemod.extract_keywords_from_text(text)
        rakeres=self.rakemod.get_ranked_phrases_with_scores()
        print("//////////////////////rakeres/////////////////")
        rakeres=rakeres[0:10]
        res=[]
        for data in rakeres:
            data = list(data)
            res.append([data[0]*10,data[1]]);
            
            
        print(res)
        print("//////////////////////yake/////////////////")
        simple_kwextractor = yake.KeywordExtractor()
        ykeywords = simple_kwextractor.extract_keywords(text)
        ykeywords = sorted(ykeywords, key=lambda a_entry: a_entry[1])
        ykeywords=ykeywords[0:10]
        for data in ykeywords:
            data = list(data)
            res.append([1/data[1],data[0]])
        res=sorted(res, key=lambda a_entry: a_entry[0],reverse=True)

        print(res)
        fres=[]
        for data in res:
            fres.append(data[1])
        fres = list(set(fres))
        return fres 
    
class starmanage:
    articlelist=[]
    def __init__(self,ArticleStar=[0.25,0.25,0.25,0.25]):
        self.articlelist=ArticleStar
    def startolist(star,modenum):
        articlelist[modenum]=articlelist[modenum]
        

#class tf_idf:
  #  tfidfDE.analyze(listArticle, 10)

