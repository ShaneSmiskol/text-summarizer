import string
import SentenceSplitter
percentage=.25 #percentage of sentences to remove, for example a value of .25 will remove 'about' 25% of the sentences and leave 75% behind
def start(text="",percentage=percentage):
    if text=="":
        text=raw_input("Enter text: ")
        print
        print "Output:"
    text=text.replace('\n',' ')
    occurancedict={}
    sentences=splitparagraph(text)
    if len(sentences)<4:
        return text
    duplicatesentences=[]
    averagesenlen=[]
    for sentence in sentences:
        averagesenlen.append(len(sentence))
        #variety=len(set(sentence))
        othersentences=list(sentences)
        othersentences.remove(sentence)
        occurance=0
        for othersentence in othersentences:
            for word in othersentence.lower().strip(string.punctuation).split():
                word
                if word.lower() in sentence.lower().strip(string.punctuation).split():
                    occurance+=1
        if occurance>len(sentence.split()):
            occurancedict[sentence]=100.0
        else:
            occurancedict[sentence]=100.0*float(occurance)/float(len(sentence.split())) #alternately, just use occurance
    averagesenlenfinal=sum(averagesenlen)/float(len(averagesenlen))
    #print occurancedict
    totalitems=len(occurancedict)
    sentencestoremovenum=int(round(totalitems*percentage,0))
    topitems=sorted(occurancedict, key=occurancedict.get, reverse=True)[:sentencestoremovenum]
    for topitem in topitems:
        sentences.remove(topitem)
    duplicatesentences=set(duplicatesentences)
    for dup in duplicatesentences:
        sentences.remove(dup)
    ''''''
    toremove=[]
    for sentence in sentences: #THIS PART IS EXPERIMENTAL!
        if len(sentence)<averagesenlenfinal:
            toremove.append(sentence)
    for i in range(len(topitems)): #THIS PART IS EXPERIMENTAL!
        try:
            sentences.remove(toremove[0])
        except:
            None
        try:
            del toremove[0]
        except:
            None
            ''''''
            
    sentences=removedups(sentences) #THIS PART IS EXPERIMENTAL!
    finaltext=' '.join(sentences)
    percentagereduced=round(abs((100.0*float(len(finaltext))/float(len(text)))-100),2)
    if str(percentagereduced)[-2:]=='.0' or str(percentagereduced)[-2:]=='00':
        reducedmessage="Reduced by: "+str(int(percentagereduced))+"%."
    elif str(percentagereduced)[-1:]=='0':
        reducedmessage="Reduced by: "+str(round(percentagereduced,1))+"%."
    else:
        reducedmessage="Reduced by: "+str(percentagereduced)+"%."
    return finaltext,reducedmessage
    
def removedups(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def splitparagraph(text):
    return SentenceSplitter.find_sentences(text)

text='Once upon a time, there was a man named Bob, and Bob had super powers. Super powers that he could not tell anyone! You know what these super powers were? Bob could fly! He could actually, really fly! Wow, what a super power! But life wasn\'t all butterflies and cupcakes, as people wanted his power. Bad people. They did everything in their power to capture Bob, but they just failed every single time. One day, though, they succeeded and they captured Bob. It turned out that all these \'bad people\' wanted was to celebrate Bob\'s Birthday! Wow, that was a relief!'
output=start(text)
print output[0]
print output[1]
