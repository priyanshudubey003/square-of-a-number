def sq_of_numbers(n):
    d=dict ()
    for i in range(1,n+1):
        if i not in d:
            d[i]=i*i
    return d
print('Squares of Number:')
z=sq_of_numbers(5)
print(z)