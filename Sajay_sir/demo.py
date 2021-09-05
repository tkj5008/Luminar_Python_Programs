# lst=[2,4,6]  #[10,8,6]
# lst=[3,5,7]  #[12,10,8]


#sumofpairs,to find the pairs which gives sum 6

# lst=[2,3,4,5]
# toal=6
# for i in lst:                         #Should avoid nested loop while programming
#     for j in lst:
#         if(i!=j):
#             if(total==i+j):
#                 print(i,j)



lst=[1,2,3,4,5]
low=0
upp=len(lst)-1
pair=6
pairs=[]
while(low<upp):
    sum=lst[low]+lst[upp]
    if(sum==pair):
        pairs.append((lst[low],lst[upp]))
        low+=1
    elif(sum>pair):
        upp-=1
    elif(sum<pair):
        low+=1
print(pairs)