txt="Natural Language Processing, or NLP, is a subdomain of artificial intelligence and focuses primarily on interpretation and generation of natural language. It helps machines or computers understand the meaning of words and phrases in user statements. The most prominent highlight in all the best NLP examples is the fact that machines can understand the context of the statement and emotions of the user."
lowercase=txt.lower()
split=lowercase.split()
my_dict={}
new_list=[]

for i in split:

  i=i.replace(".","")
  i=i.replace(",","")
  new_list.append(i)

for i in new_list:
  if i in my_dict:
    my_dict[i] +=1


  else:
      my_dict[i] =1
print(my_dict)

