'''
Man and computer play rock-paper-scissors guessing game
@Author:grand li
@Date: 1:07 2020/10/20
'''

'''
Algorithm introduction:

1.Mapping rock-paper-scissors into specific integers; Such as scissors-0, rock-1, cloth-2
2.Perform difference calculation between the punch value given by human and computer;
3.The results are: 
a. In a tie (scissors-scissors, rock-rock, cloth-cloth) the difference is 0; 
b. When a person wins (scissors-cloth, rock-scissors, cloth-rock) the difference is -2, 1, 1; 
c. When the person is negative (scissors-rock, rock-cloth, cloth-scissors), the difference is -1, -1, 2;
4.Only judge the difference and get the result of the guessing box;
'''

#!/usr/bin/python
import random


def translate(vote):
    if ('剪刀' == vote):
        tran = 0
    elif ('石头' == vote):
        tran = 1
    elif ('布' == vote):
        tran = 2
    else:
        #print('异常')
        tran = 10
    return tran

#电脑出拳
def computer_choice():   
    randC = random.uniform(0, 3)
    if (randC > 2):
        voteC = "布"
        value = 2
    elif (randC > 1):
        voteC = "石头"
        value = 1
    else:
        voteC = "剪刀"
        value = 0
    return voteC, value

#结果输出
def rule(diff):
    if (0 == diff):
        print('平局')
    elif ((-2 == diff) or (1 == diff)):
        print('人胜')
    elif ((-1 == diff) or (2 == diff)):
        print('人负')
    else:
        print('异常')


class guess(object):
    def __init__(self, vote, value):
        self.vote = vote
        self.value = value
    def __str__(self):
        return "vote:%s value:%d" % \
            ( self.vote, self.value)

person = guess('none', 10)
computer = guess('none', 10)

person.vote = input("请出拳[剪刀、石头、布]")       
person.value = translate(person.vote)

computer.vote, computer.value = computer_choice()

diff = person.value - computer.value
#print(diff)
rule(diff)

#print(person)
#print(computer)




    

            
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    