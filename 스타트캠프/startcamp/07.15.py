num1=3.14  #실수
print(type(num1))

name='hi'
bye=f'{name}is my name'
print(bye)

######
food=['rice','cake','sushi']
food.append('noodle')
print(food[0])

food[1]='초밥'
print(food)

#######
my_home ={'location':'seoul','area':'052'}

# print(my_home['location'])
# print(my_home.get('location2','navy')) ##---> none



#---------------------
my_home['park']='red'
print(my_home)

my_home['park']='pink princess' #----> 변경 가능
print(my_home)
