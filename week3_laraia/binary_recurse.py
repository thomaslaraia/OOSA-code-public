def binaryRecurse(x,v,start,end):
  '''Binary search for v in x by recursion'''

  ind = (start+end)//2
  thisVal=x[ind]

  if((end-start)<=1):
    return(thisVal,ind)

  if(thisVal<v):
    thisVal,ind=binaryRecurse(x,v,ind,end)
  elif(thisVal>v):
    thisVal,ind=binaryRecurse(x,v,start,ind)
  elif(thisVal==v):
    return(thisVal,ind)

  return(thisVal,ind)
