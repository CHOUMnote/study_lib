def quickSort(arr):
    if len(arr) <= 1: 
        return arr
    
    pivot = arr[len(arr)//2]    #피봇 = 중간
    less = []
    more = []
    equal = []
    for a in arr:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)
    
    return quickSort(less) + equal + quickSort(more)
    
    '''
    피봇 : 중간
    장점 : 직관적이다. 배열을 하나 넘겨서 따로 정렬 안하고 배열 하나에 큰거 끼리, 작은거 끼리 묶어서 리턴 하기 때문에 직관 적이다.
    단점 : 배열을 3개나 만들어야 하기 대문에 스왑 방식에 비해 메모리 소모가 크다.
    '''
