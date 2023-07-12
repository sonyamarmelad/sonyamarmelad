def chunk(list, size):
    return [list[i:i+size] for i in range(0, len(list), size)]


lst = [i for i in range(25)]


chunk(lst, 7)
>>> [[0, 1, 2, 3, 4, 5, 6], 
    [7, 8, 9, 10, 11, 12, 13],  
    [14, 15, 16, 17, 18, 19, 20],  
    [21, 22, 23, 24]]
