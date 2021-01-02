import sys 
import os
import itertools
import enchant

def main():
	#clear the screen
	os.system('cls' if os.name == 'nt' else 'clear')

	#set the dict 
	d = enchant.Dict("en_US")
	wLn = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #wordLength: 15 letters max

	#iterate letter index - word length
	for ldx in wLn:
	    ans = []
	    ##ppermutations: arg=p[, r] res=r-length tuples, all possible orderings, no repeated elements 
	    for l in itertools.permutations(list(sys.argv[1]), ldx): 
	        w = "".join(l)      #combine letters > word(w)
	        if d.check(w):      #check if the word is in the dictionary
	            ans.append(w)   #add the word to the answer(ans) list
	    ans.sort()              #sort the list in ascending order
	    for i in ans:           #iterate through all words found & 
	        print(i)        	#print the list


if __name__ == "__main__":
	main()


