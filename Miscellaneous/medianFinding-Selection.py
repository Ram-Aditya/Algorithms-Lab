from collections import defaultdict

def Selection(a,k):
    if(len(a)!=1):
        freq=defaultdict(int)
        med=approxMed(a)
        al=[]
        ar=[]
        for i in a:
            freq[i]=freq[i]+1
            if(i<= med):
                al.append(i)
            elif (i>med):
                ar.append(i)
        if(freq[med]==1 and len(al)==(k)):
            return med
        elif(freq[med]>1 and freq[med]>=(k-(len(al)-freq[med]))):
            return med
        elif(freq[med]==1 and len(al)>(k)):
            return Selection(al,k)
        else:
            return Selection(ar,k-1-len(al))
    else:
        return a[0]

def approxMed(arr):
        j=0
        barr=[]
        for i in range(len(arr)//5):
            t=sort(arr[j:j+5])
            barr.append(t[2])
            j=j+5
        if(len(arr)%5!=0):
            t=sort(arr[(len(arr)//5)*5:])
            barr.append(t[(len(t)+1)//2-1])
        return Selection(barr,(len(barr)+1)//2)

def sort(ar):
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if(ar[i]>ar[j]):
                ar[j],ar[i]=ar[i],ar[j]
    return ar

L=input("Enter List: ")
L=L.split()
t=[]
for i in L:
    t.append(int(i))
print(Selection(t,(len(t)+1)//2))
