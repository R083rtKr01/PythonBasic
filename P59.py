from random import randint

sentence="Niektórzy przyzwyczaili się już może, że w światowej piłce są tylko dwie postacie – Messi oraz Ronaldo –" \
         " zgarniające najbardziej prestiżowe indywidualne nagrody. Robert Lewandowski strzela mnóstwo goli, ale " \
         "najwidoczniej to wciąż za mało. Jak mówiłem, niektórzy się może przyzwyczaili do wyborów albo kartki im się" \
         " posklejały – mówi o wczesnych wynikach Złotej Piłki Jacek Krzynówek, były reprezentant Polski."
def sentenceGenerator(sentence, n=5):
    sentence=sentence.replace(",","").replace(".","").replace("-","")
    words=sentence.split(" ")
    resultSentence = ""
    #generowanie nowego randomowego zdania o określonej liczbie słów
    for i in range(n):
        resultSentence+=words[randint(0,len(words)-1)]+" "
    resultSentence = resultSentence[0: len(resultSentence)-1]+"."
    return resultSentence
print(sentenceGenerator(sentence))
print(sentenceGenerator(sentence,n=10))
