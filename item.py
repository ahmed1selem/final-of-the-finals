from scraping import init
from classifier import get_cat
from summarizer import summarize
class paragraph:
   def __init__(self,url):
       self.url=url
       self.cleaned=""
       self.title=""
       self.summary=""
       self.img=""
       self.scrap()
   def scrap(self):
       self.cleaned,self.title,self.img=init(self.url)
       if not self.cleaned:
                self.cleaned=self.title

   def get_cleaned(self):
       return self.cleaned
   def get_title(self):
       return self.title
   def get_cat(self):
     return get_cat(self.cleaned)
   def get_summary(self):
       print(self.cleaned)
       if not self.cleaned or self.cleaned ==self.title:
                return self.title
       else:
            summ=summarize(self.cleaned)
            return summ
   def get_img(self):
       return self.img





   
