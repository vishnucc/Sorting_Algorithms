def binary_search(array,start,end,element_to_search):
    if end>=start:
        middle_Value_position=start+(end-start)//2
        if array[middle_Value_position]==element_to_search:
            return middle_Value_position
        elif element_to_search>array[middle_Value_position]:
            return binary_search(array,middle_Value_position+1,end,element_to_search)
        else:
            return binary_search(array,start,middle_Value_position-1,element_to_search)
    else:
        return -1
    
array=[0,5,6,7,8,9]
element_to_search=int(input("Enter element to be searched :"))

if binary_search(array,0,len(array)-1,element_to_search)==-1:
    print("Element is not in array")
else:
    print("Element is in array and is at",binary_search(array,0,len(array)-1,element_to_search))
     
        
# def sort_array_elements(a):
#     """bubble sort
#         This function will sort the array elements in ascending order
#     """
#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]>=a[j]:
#                 a[i],a[j]=a[j],a[i]
#     return a

# def quick_sort(array):
#     if (len(array)<=1): 
#         return array[0]
#     else:
#         pivot = array[len(array)//2]
#         left_array=[element for element in array if element<pivot]
#         right_array=[element for element in array if element>pivot]
#         middle_element=[element for element in array if element==pivot]
#         return quick_sort(left_array) + middle_element + quick_sort(right_array)


# array=[10,36,100.25,25,2,3,5,6,9,10]
# n=len(array)

# x=10
# print(binary_search(array,0,n-1,x))
# print(sort_array_elements.__doc__)
