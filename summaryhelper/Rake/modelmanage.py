import tfidfDE
from rake_nltk import Rake
from summa import keywords
import yake


class starmanage:
    def __init__(self,ArticleStar):
        self.starscore=ArticleStar

    def get_starscore(self):
        return self.starscore

    def update_starscore(self,stars):
        self.starscore=self.starscore+(stars-3)*0.01


class extractkeyword:

    def __init__(self):
        self.rakemod = Rake()
        self.starscore = starmanage(1)
        self.rakeweight = 10

    def update_starscore(self, stars):
        """
        Utility function to update startscore
        @param user result of star
        """
        self.starscore.update_starscore(stars)

    def get_Keyword(self, text):
        """
        Utility function to get keyword by using two keyword extract algorithm
        @param user input(string)
        @return list A list of keywords
        """

        self.rakemod.extract_keywords_from_text(text)
        rakeres=self.rakemod.get_ranked_phrases_with_scores()
        print("//////////////////////rakeres/////////////////")
        rakeres=rakeres[0:10]
        res=[]
        for data in rakeres:
            data = list(data)
            if 20-self.rakeweight is not 0:
                res.append([data[0]*((9+(self.starscore.get_starscore()/2)*(1+20/self.rakeweight))),data[1]])
            
        print(res)
        print("//////////////////////yake/////////////////")
        simple_kwextractor = yake.KeywordExtractor()
        ykeywords = simple_kwextractor.extract_keywords(text)
        ykeywords = sorted(ykeywords, key=lambda a_entry: a_entry[1])
        ykeywords=ykeywords[0:10]
        print(ykeywords)
        for data in ykeywords:
            data = list(data)
            if 20-self.rakeweight is not 0:
                res.append([1/data[1]*1/2*(1+20/(20-self.rakeweight)),data[0]])

        res=sorted(res, key=lambda a_entry: a_entry[0],reverse=True)
        fres=[]
        for data in res:
            fres.append(data[1])
        fres = list(set(fres))
        if len(fres) >5:
           fres=fres[:5]

        self.rakeweight=10
        for result in fres:
            if set(result) & set(fres) is not set():
                self.rakeweight=self.rakeweight+1

        return fres 

