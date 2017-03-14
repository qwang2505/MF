'''
Created on: May 06, 2014

@author: qwang
'''

def binary_search(array, elem):
    pass

def find(array, elem):
    mid_index = len(array) / 2
    start = array[0]
    end = array[-1]
    mid = array[mid]
    if start <= mid and mid <= end:
        # sorted, find by binary search
        return binary_search(array, elem)
    elif start <= mid and mid >= end:
        # first half sorted, recursilly get sorted half
        if elem >= start and elem <= mid:
            return binary_serach(array[0:mid_index+1], elem)
        else:
            return find(array[mid_index:-1])
    elif end >= mid and mid >= start:
        # second half sorted, recursilly get sorted half
        if elem >= mid and elem <= end:
            return binary_search(array[mid_index:-1], elem)
        else:
            return find(array[0:mid_index+1], elem)

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, -3, -2, -1]
    elem = -3
