def merge(l1,l2):
    l3=[];
    INFINITY=99999999;
    l1.append(INFINITY);
    l2.append(INFINITY);
    lkey=0;
    rkey=0;
    while not(l1[lkey]==INFINITY and l2[rkey]==INFINITY) :
        if l1[lkey]>l2[rkey] :
            l3.append(l2[rkey]);
            rkey+=1;
        else :
            l3.append(l1[lkey]);
            lkey+=1;
          
    return l3
    
    
    
def mergeSort(l):
    if(len(l)==1):
        return l;  
    else:
        print("partition at "+str(int(len(l)/2))+" and "+str(int(len(l)/2)+1));
        left=mergeSort(l[:int(len(l)/2)]);
        right=mergeSort(l[int(len(l)/2+1):]);
        return merge(left,right);
        
def max(n1,n2,l):
    try :
        if l[n1]>l[n2] :
            return n1;
    except :
        return n1;
    return n2;
    
def min(n1,n2,l):
    try :
        if l[n1]>l[n2] :
            return n2;
    except :
        return n1;
    return n1;
            

        
def Maxheapify(l,i):
    if i>int(len(l)/2) :
        return;
    key=max(max(i,2*i,l),2*i+1,l);
    if key == i:
        return;
    l[i]+=l[key];
    l[key]=l[i]-l[key];
    l[i]=l[i]-l[key];
    Maxheapify(l,key);

def Minheapify(l,i):
    if i>int(len(l)/2) :
        return;
    key=min(min(i,2*i,l),2*i+1,l);
    if key == i:
        return;
    l[i]+=l[key];
    l[key]=l[i]-l[key];
    l[i]=l[i]-l[key];
    Minheapify(l,key);
    
def makeMaxHeap(l):
    for i in range(int((len(l)-1)/2),0,-1):
        Maxheapify(l,i);
        
def makeMinHeap(l):
    for i in range(int((len(l)-1)/2),0,-1):
        Minheapify(l,i);

    
l=[0,2,3,34,76,100,50,4,5,21,69];
makeMaxHeap(l) 
makeMaxHeap(l)
print(l);
	



