
#

def Buble_Sort(elements):
    #  Outer loop to iterate through the list n times
    for n in range(len(elements) -1,0,-1):
        swapped = False
        #   Inner loop to compare adjacent elements
        for i in range(n):
            if elements[i] > elements[i+1]:
                #swap elements if they're in wrong order
                swapped = True
                elements[i], elements[i+1] = elements[i+1], elements[i]
                # If we didn't make any swaps in a pass, the list is already sorted and we can exit the outer loop.
                if not swapped:
                    return

elements = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted List Is: ")
print(elements)

Buble_Sort(elements)

print("Sorted list is:")
print(elements)


