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
    time = ""
    time_found = False
    for subtree in tree.subtrees():
        if subtree.label() == 'CD':
            time = ''.join(str(x) for x in subtree.leaves())
            time_found = True
        if time_found and subtree.label() == 'NN':
            s = ''.join(x for x in subtree.leaves())
            if s == 'evening' or s == 'pm':
                time = str(int(time[:time.index(':')])+12)+time[-3:]
    return time


def getDate(text):
    subtrees = list((list(parser.raw_parse(text))[0]).subtrees())
    day = 0
    year = 0
    month = 0
    msg = ""
    msg_found = 0
    for i in range(len(subtrees)):
        if subtrees[i].label() == 'JJ':
            day = int(''.join(str(x) for x in subtrees[i].leaves())[:2])
            year = int(''.join(str(x) for x in subtrees[i+2].leaves()))
            month = int(strptime(''.join(str(x) for x in subtrees[i+1].leaves())[:3], '%b').tm_mon)
        if subtrees[i].label() == 'NP':
            msg_found += 1
            if msg_found == 3 or msg_found == 4:
                msg = ' '.join(str(x) for x in subtrees[i].leaves())
    return year, month, day, msg


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


# format should be similar
print getDate("Set reminder for Tanmay's birthday on 14th November 2017")
print getAlarmTime("set an alarm for 5:30 in the evening")
