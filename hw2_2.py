nums_odd=[]
num=1
while num < 100:
  if num % 2 !=0 :
    nums_odd.append(num)
  num +=1
print(nums_odd)

step_4=[]
for i in range(1,100):
  if i % 2 !=0:
    step_4.append(i)

print(step_4[::4])

my_list=["maryam","mohammad","ali","raha","mina"]
rvs_list=[]

for i in reversed(step_4[::4]):
  rvs_list.append(i)

print(my_list+rvs_list)
