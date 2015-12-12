# append/join


>>> strs = []
>>> for x in range(10):
...     strs.append(str(x))
... 
>>> strs
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> "".join(strs)
'0123456789'