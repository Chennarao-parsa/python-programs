#flatten a list
'''
l=[[1,2],[3,4],[5,6],{2,4},(1,9),[8,0],[0]]

def flatten(l):
    output=[]
    for i in l:
        if isinstance(i,(list,tuple,set)):
            output.extend(flatten(i))
        else:
            output.append(i)
    return output

res=flatten(l)
print(res)
'''
l=[[1,2],[3,4],[5,6],{2,4},[8,0],[0]]
def flatten(l):
    output=[]
    for i in l:
       
        if isinstance(i,(list,tuple,set)):
            output.extend(flatten(i))
        else:
            output.append(i)
    return output

res=flatten(l)
print(res)

