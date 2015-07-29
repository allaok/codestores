from ProblemSet7.NewStory import NewsStory
from ProblemSet7.ps7 import Trigger
import string
__author__ = 'root'
class WordTrigger(Trigger):
    def __init__(self,word):
        self.word=word

    def isWordIn(self,text):
        text_without_punctuation=self.replace_punctuation(text)
        words=text_without_punctuation.split(' ')
        for w in words:

            if self.word.lower() == w.lower():
                return True

        return False


    def replace_punctuation(self,text):
        new_text=text
        #print string.punctuation
        punctuations=string.punctuation
        for s in punctuations:
              #print 'PUNCTUATION=',s
              new_text=new_text.replace(s,' ')
        #print 'NEW TEXT=', new_text
        return new_text



class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SummaryTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


class SubjectTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger=trigger
    def evaluate(self,story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1=trigger1
        self.trigger2=trigger2
    def evaluate(self,story):
        return  self.trigger1.evaluate(story)  and self.trigger2.evaluate(story)

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1=trigger1
        self.trigger2=trigger2
    def evaluate(self,story):
        return  self.trigger1.evaluate(story)  or self.trigger2.evaluate(story)



class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase=phrase
    def evaluate(self,story):
        #or_trigger=OrTrigger(OrTrigger(TitleTrigger(self.phrase),SubjectTrigger(self.phrase)),SummaryTrigger(self.phrase))
        return self.phrase in story.getSubject() or self.phrase in story.getSummary() or self.phrase in story.getTitle()





if __name__ == '__main__':
     test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
     title_trigger=TitleTrigger(test)
     print title_trigger.replace_punctuation('Bonjour!,;Aurevoir:Voir,;,?Revoir')