import itertools
import time
import os
def brute_force(wordlist,password):
    for attempt in wordlist:
        if attempt==password:
            print(f"password is : {attempt}")
        else:
            print('password not found')
target_password=input('enter password for brute force attack:')
wordlist_file=input('enter wordlist file path:')
with open(wordlist_file,'r') as file:
    wordlist=file.read().splitlines()
start_time=time.time()
brute_force(wordlist,target_password)
end_time=time.time()
print(f"brute force attack completed in {end_time - start_time} seconds")