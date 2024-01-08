#a = 2
#print(a)
#a = a+4
#print(a)
#b="leon"
#print(b)
#c=[1,2,3]
#print(c[-1])

def my_function_b():
    c = 4
    c = c + 2
    print(c)

def my_function():
    c = 4
    print(c)

def get_name():
    return "nikita"

def add(x, y):
    return x + y

def mul(a, b):
    return a * b

def printX(x):
    a = 0
    while a <= x:
        print(a)
        a=a+1
def PrintArray(x):
    a=0
    while a < len(x):
        print(x[a])
        a=a+1



# 1) reverse array - return new reversed array
# 2) does array contain element
# multiply array - array, number s



def does_list_of_boxes_contains_toy(list_of_boxes, toy):
    current_box_number = 0
    length_of_box =len(list_of_boxes)
    while current_box_number != length_of_box:
        current_box_number += 1
        if list_of_boxes[current_box_number] == toy:
            return True

    return False

def Mul_array(array, multyplyer):
    legnth_of_array = len(array)
    curent_num = 0
    while curent_num != legnth_of_array:
        x = mul(array[curent_num],multyplyer)
        array[curent_num]=x
        curent_num += 1
    return array

def reverse_array(array):
    a = 0
    b = len(array)- 1
    while b >= a:
        array[a],array[b] = array[b], array[a]
        a += 1
        b -= 1
    return array

result = reverse_array([1,2,3])
##print(result)

def reverse_array(array):
    reversed_list= []
    a = len(array) - 1
    while a >= 0:
        item = array[a]
        reversed_list.append(item)
        a -= 1
    return reversed_list

result = reverse_array([7,4,2,9])
print(result)
        

##result = does_list_of_boxes_contains_toy([1,2,3,4,5,6,7,8,9,10,], 70)
##
##print(result)

##esult = Mul_array([1,2,3,4],2)
##print(result)
##    while y != x[len(x)-b]:
##        if b= len(x)-1:
##            print("nope")
##        else:
##            print("yep")

a = 0
  



#my_function()
#my_function_b()
##v = get_name()
##print(v)
##
##c = add(1, 2)
##
##print(c)
##
##n= mul(3,4)
##printX(10)
##print (n)
##PrintArray([1,2,3])
##
##x = [1,2,3]
##x[0]
##x[1]
##x[2]
##
##x[3]
##
##len(x)
