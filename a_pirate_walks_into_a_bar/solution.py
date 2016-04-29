def answer(numbers):
  #traverse the sequence , from pirate to pirate, track in n the count of iterations, 
  def t(arr,s,g,n):
    g = arr[g]
    if (g==s):
      return n+1
    else:
      n=n+1
      return t(arr,s,g,n)

  #generate list containing the duplicate entry in numbers
  mylist = [x for x in numbers if numbers.count(x) > 1]
  if len(mylist)==0:  #there are no duplicate entries, then answer is 0
    return 0

  num = mylist.pop() 
  return t(numbers,num,num,0)
