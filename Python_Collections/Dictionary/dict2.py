count={}
data=input("Enter")
words=data.split(" ")
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)