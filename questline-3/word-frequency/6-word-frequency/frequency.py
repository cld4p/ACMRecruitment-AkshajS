
f=open("word-frequency/input.txt")
fWrite=open("word-frequency/output.txt","w")

l=f.read()
words={}

for i in l.split():
    if i.lower() not in words:
        words[i.lower()]=1
    else:
        words[i.lower().rstrip("\n")]+=1

sorted_words = {word: amount for word, amount in sorted(words.items(), key=lambda item: item[1], reverse=True)}

for i in sorted_words.keys():
    fWrite.write(i+" -> "+str(words[i])+"\n")


f.close()
