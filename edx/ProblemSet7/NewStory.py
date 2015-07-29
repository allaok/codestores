from ProblemSet7 import ps7

__author__ = 'root'

from ps7 import *

class NewsStory(object):
    def __init__(self,guid, title, subject, summary, link):
        self.guid=guid
        self.title=title
        self.subject=subject
        self.summary=summary
        self.link=link

    def getGuid(self):
        return self.guid


    def getTitle(self):
        return self.title


    def getSubject(self):
        return self.subject


    def getSummary(self):
        return self.summary


    def getLink(self): return self.link

test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
print test.getGuid()
test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
