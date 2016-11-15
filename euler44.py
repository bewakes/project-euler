# the logic  is to proceed from the initial pentagonal numbers and check backwards

num_hash = [1,0,0,0,1,0,0,0,0,0,0,1]
pentagonals = [1,5,12]
len_hash =12 

n = 4 # now the turn of fourth pentagonal number

pent_index = 2 # we start with 12
while True:
    flag = False
    decr = pent_index -1 # we will start with 5 and proceed backwards
    while True:
        small1 = pentagonals[decr]
        small2 = pentagonals[pent_index] - pentagonals[decr]
        if num_hash[small2-1]: # means small1 and small2 sum to pentagonal , now check diff of small1 and small2
            diff = small1 - small2
            if diff!=0 and num_hash[diff-1]:
                print small1, small2, small1-small2
                flag=True
                break
        decr-=1
        if decr < 2 or small1+pentagonals[decr] < pentagonals[pent_index]:
            break
    if flag:
        break
    # now create new pentagonal number
    new = n*(3*n-1)/2
    num_hash_incr = new - len_hash
    num_hash.extend(0 for x in range(num_hash_incr-1)) # all the intermediate numbers are not pentagonal
    # the last one is pentagonal
    num_hash.append(1)
    pentagonals.append(new)
    pent_index+=1
    len_hash+= num_hash_incr
    n+=1
    #print num_hash


