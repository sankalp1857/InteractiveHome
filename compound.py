import os
from nltk.parse.stanford import StanfordParser
from time import strptime

os.environ['CLASSPATH'] += ":/media/windows/Users/maytan/Documents/libs/stanford-parser/"

parser = StanfordParser()


def checkCompound(text):
    tree = list(parser.raw_parse(text))[0]
    for subtree in tree.subtrees():
        if subtree.label() == 'CC':
            return True
    return False


def getAlarmTime(text):
    tree = list(parser.raw_parse(text))[0]
    for subtree in tree.subtrees():
        if subtree.label() == 'CD':
            return ' '.join(str(x) for x in subtree.leaves())


def getDate(text):
    subtrees = list((list(parser.raw_parse(text))[0]).subtrees())

    for i in range(len(subtrees)):
        if subtrees[i].label() == 'CD':
            day = int(''.join(str(x) for x in subtrees[i].leaves()))
            month = ' '.join(str(x) for x in subtrees[i+1].leaves())
            year = int(month.split(' ')[1])
            month = int(strptime(month.split(' ')[0][:3], '%b').tm_mon)
            return year, month, day


def traverseTree(text):
    tree = list(parser.raw_parse(text))[0]
    subtrees = list(tree.subtrees())
    if checkCompound(text):
        subtrees = subtrees[3:]
    else:
        subtrees = subtrees[2:]

    for subtree in subtrees:
        if subtree.label() == 'VP':
            print ' '.join(str(x) for x in subtree.leaves())


print getDate("set a reminder for sankalp's birthday on 19 January 2018")
print getAlarmTime("set an alarm for 5:30 pm")
