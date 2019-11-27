sentence = "Ala ma kota, kot ma Ale."
# oczyścic ze znaków interpunkcyjnych

sentence = sentence.replace(",","")
sentence = sentence.replace(".","")
print(sentence)

#zapisz wszystkie słowa w zdaniu w liście words
words = sentence.split(" ")
print(words)

