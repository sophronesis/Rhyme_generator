def main():
	from collections import Counter
	from sys import argv
	from random import shuffle
	top_amount = 25
	to_shuffle = False
	if len(argv)>1:
		top_amount = int(argv[1])
	if len(argv)>2:
		if argv[2]=='True' or argv[2]=='1' or argv[2]=='true':
			to_shuffle = True
	#loading data
	data = open('text8','r').read()
	print("Loaded words data")
	prepared = Counter(data.split())
	while(True):
		rhyme = input("input rhyme:\n")
		rev_rhyme = rhyme[::-1]
		result = filter(lambda x:x[0][0][-len(rhyme):]==rhyme,zip(prepared.most_common()))
		result = list(map(lambda x:x[0],result))
		if to_shuffle:
			shuffle(result)
		if len(result)>0:
			actual_ammount = len(result) if top_amount==-1 else min(top_amount,len(result))
			print("Top {} rhyme words:".format(actual_ammount))
			for i in result[:actual_ammount]:
				print("{:10} | {}".format(i[1],i[0]))
		else: print("No rhymes found")

if __name__ == '__main__':
	main()
