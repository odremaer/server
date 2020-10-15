def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <=pivot]
        print('{}{}'.format(less, 'less'))
        greater = [i for i in array [1:] if i > pivot]
        print('{}{}'.format(greater, 'greater'))
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([6,4,5,1,2,3,7,8,9]))