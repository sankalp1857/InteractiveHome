import os
from nltk.tree import ParentedTree
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
    tree = ParentedTree.convert(list(parser.raw_parse(text))[0])
    subtrees = list(tree.subtrees())
    day = 0
    year = 0
    month = 0
    cat = 0

    for i in range(len(subtrees)):
        if subtrees[i].label() == 'JJ':
            day = int(''.join(str(x) for x in subtrees[i].leaves())[:2])
            parent = subtrees[i].parent()
            cat = len(subtrees[i].parent().leaves())
            if cat == 1:
                year = int(parent.parent().leaves()[2])
                month = int(strptime(parent.parent().leaves()[1][:3], '%b').tm_mon)
            else:
                year = int(parent.leaves()[2])
                month = int(strptime(parent.leaves()[1][:3], '%b').tm_mon)

    return year, month, day, cat


def getMessage(text, cat):
    tree = ParentedTree.convert(list(parser.raw_parse(text))[0])
    phrases_passed = 0
    for subtree in tree.subtrees():
        if subtree.label() == 'NP' or subtree.label() == 'VP':
            phrases_passed += 1
            if cat == 1 and phrases_passed == 6:
                return ' '.join(x for x in subtree.leaves())
            elif cat == 3 and phrases_passed == 3:
                total = [str(x) for x in subtree.leaves()]
                subtree = list(subtree.subtrees(filter=lambda x: x.label() == "PP"))[0]
                pre = [str(x) for x in subtree.leaves()]
                return ' '.join(x for x in [word for word in total if word not in pre])


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
text = "Set reminder to buy a gift on 14th November 2017"
year, month, day, category = getDate(text)
msg = getMessage(text, category)
print year, month, day, msg
print getAlarmTime("set an alarm for 5:30 in the evening")
