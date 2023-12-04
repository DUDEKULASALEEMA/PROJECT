def get_sum_second_largest(even_matrix,odd_matrix):
    #function to calculate the sum of second-largest number from 
    # check if even matri has at least two elements
    if len(even_matrix)>=2:
        even_second_largest=even_matrix[-2]
    else:
        even_second_largest = float('-inf')
    #check if odd matrix hasat least two elements
    if len(odd_matrix) >=2:
        odd_second_largest = odd_matrix[-2]
    else:
        odd_second_largest = float('-inif')
    #return the sum of second-largest numbers
    return even_second_largest +odd_second_largest
#input size of the matrix
size =int(input("enter the size of arry: "))
#input elements of the matrix
matrix = []
for i in range(size):
    element = int(input(f"enter element a {i} index: "))
    matrix.append(element)
    #divide the matrix into even and odd sub-marices
even_matrix =matrix[::2] #elements at even indices
odd_matrix =matrix[1::2]#elements at odd indices
#sort even and odd matrices in ascending order
even_matrix.sort()
odd_matrix.sort()
#print sorted matrices
print(f"sorted even array: {even_matrix}")
print(f"sorted odd array: {odd_matrix}")
#calculate and print the sum of second_largest numbers
sum_second_largest =  get_sum_second_largest(even_matrix,odd_matrix)
print(f"sum of second-largest numbers :{sum_second_largest}" )