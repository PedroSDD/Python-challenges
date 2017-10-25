'''
Binary to Decimal and Back Converter - Develop a converter to convert a decimal number 
to binary or a binary number to its decimal equivalent.

'''
import math 

def binToDec(binary_number):
	binary_number_list = (map(int, str(binary_number)))
	# decimal = 0

	# for i, item in enumerate(binary_number_list):
	# 	if item == 1:
	# 		print ((len(binary_number_list)-i)-1)
	# 		decimal += math.pow(2,((len(binary_number_list)-i)-1))
	# return decimal


	print sum(map(lambda x, y: x, y=len(binary_number_list) if x != 1 y+=1 else (math.pow(2,(len(binary_number_list))-1)) y-=1 , binary_number_list))



	


	#return map(lambda x: x if x < len(population) else (lenpopulation)-x)*-1, indexes)

def main():
    binToDec(110)

if __name__ == "__main__":
    main()
