import sys
import numpy
from collections import defaultdict


def get_max_profit(details,total_gold,total_jewel,index,memoizeddp):

    if index==total_jewel:
        return 0

    key= str(total_gold)+'|'+str(index)

    if memoizeddp[key] !=0:
        return memoizeddp[key]

    possible_number_of_jewel= total_gold/details[index][1]
    possible_number_of_jewel=min(possible_number_of_jewel,details[index][4])

    if total_gold==0 or possible_number_of_jewel==0:
        return get_max_profit(details,total_gold,total_jewel,index+1,memoizeddp)-min((details[index][5]*(details[index][3]-0)),details[index][6])


    total_profit = -sys.maxint

    for amount in range(0,possible_number_of_jewel+1):

        if amount<details[index][3]:
            fine= min((details[index][5]*(details[index][3]-amount)),details[index][6])
        else:
            fine=0

        if (total_gold - (amount * details[index][1]))>=0:
            profit= amount*details[index][2]-fine+get_max_profit(details,total_gold-(amount*details[index][1]),total_jewel,index+1,memoizeddp)

        if total_profit<profit:
            total_profit=profit


    memoizeddp[key]=total_profit
    return memoizeddp[key]



def get_max_profit_dp(details,total_gold,total_jewel):

    dp=[[0 for x in range(total_jewel)] for x in range(total_gold+1)]
    path=[[1 for x in range(total_jewel)] for x in range(total_gold+1)]


    #for first column of matrix
    for gold in range(0,total_gold+1):

        # find max quantity possible using available gold
        quantity=gold / details[0][1]

        #create fine accordingly based on quantity and constraint given in input
        if quantity < details[0][3]:
            fine = min((details[0][5] * (details[0][3] - quantity)), details[0][6])
        else:
            fine = 0
        dp[gold][0] = quantity*details[0][2]-fine


    # for first row of matrix, keep adding fines if any + previous profit
    for jewel in range(1,total_jewel):
        dp[0][jewel] =dp[0][jewel-1]-min((details[jewel][5]*(details[jewel][3]-0)),details[jewel][6])


    for gold in range(1,total_gold+1):

        for jewel in range(1,total_jewel):

            # find quantity possible using available gold and allowed quantity
            possible_number_of_jewel = gold / details[jewel][1]
            possible_number_of_jewel = min(possible_number_of_jewel, details[jewel][4])

            if possible_number_of_jewel==0:
                dp[gold][jewel]=dp[gold][jewel-1]-min((details[jewel][5] * (details[jewel][3] - 0)), details[jewel][6])
                path[gold][jewel] += path[gold][jewel-1]
            else:

                temp=-sys.maxint
                for i in range(0,possible_number_of_jewel+1):

                    # create fine accordingly if quantity is less that min quantity possible
                    if i < details[jewel][3]:
                        fine = min((details[jewel][5] * (details[jewel][3] - i)), details[jewel][6])
                    else:
                        fine = 0

                    #find profit for every quantity
                    local_max=  i * details[jewel][2]-fine+dp[gold-i*details[jewel][1]][jewel-1]


                    if temp==local_max:
                        path[gold][jewel] += path[gold-i*details[jewel][1]][jewel - 1]

                    #update the global max for this particular jewellery
                    if temp<local_max:
                        temp=local_max
                        path[gold][jewel] = path[gold - i * details[jewel][1]][jewel - 1]


                dp[gold][jewel]=temp


    print ''
    print  dp[total_gold][total_jewel-1], path[total_gold][total_jewel-1]
    return  dp[total_gold][total_jewel-1]




def get_path(details,total_gold,total_jewel,index,result,source,destination):

    if  source==destination and index==total_jewel:
        print result[:]
        return

    if index==total_jewel:
        return

    if source==destination and index<total_jewel-1:
        result.append(0)
        get_path(details,total_gold,total_jewel,index+1,result,source,destination)
        result.pop()
        return

    possible_number_of_jewel = total_gold / details[index][1]
    possible_number_of_jewel = min(possible_number_of_jewel, details[index][4])


    for amount in range(0,possible_number_of_jewel+1):

        if amount<details[index][3]:
            fine= min((details[index][5]*(details[index][3]-amount)),details[index][6])
        else:
            fine=0

        result.append(amount)
        source=source+amount*details[index][2]-fine
        get_path(details,total_gold-(amount*details[index][1]),total_jewel,index+1,result,source,destination)
        source=source-(amount*details[index][2]-fine)
        result.pop()








'''

Creating input details array based of input source, either from file or console
details will be an array of arrays, that will contain all information
about jewellery 

For example : 
for below mentioned input 
20 2
1 2 10 8 10 2 2
2 2 10 8 10 2 4

details will be like this,

[[1,2,10,8,2,2],[2,2,10,8,10,2,4]]

'''

if len(sys.argv)==1 or sys.argv[1]=='-':

    val1= map(int,raw_input().split())
    total_gold=val1[0]
    total_jewel=val1[1]
    details=[]
    for i in range(0,total_jewel):
        val2=map(int,raw_input().split())
        details.append(val2)

else:

    fname=sys.argv[1]
    fh = open(fname,"r")

    val1 = map(int, fh.readline().split())
    total_gold = val1[0]
    total_jewel = val1[1]
    details = []
    for i in range(0, total_jewel):
        val2 = map(int, fh.readline().split())
        details.append(val2)
    fh.close()



#Creating datastructures that will help us to make memoized dp and  printing path
memoizeddp=defaultdict(int)
result = []
source = 0


#Calling dp program, it will print max_profit,path first and then return maxprofit
max_profit= get_max_profit_dp(details,total_gold,total_jewel)
des = max_profit


#printing path , if required command given, source =0,destination=max_profit
if len(sys.argv)>2 and int(sys.argv[2]) > 0:
    get_path(details, total_gold, total_jewel, 0, result, source, des)





#memoized call
#print get_max_profit(details,total_gold,total_jewel,0,memoizeddp)




