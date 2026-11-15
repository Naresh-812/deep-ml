def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    d=[]
    s=0
    for i in a:
        for x,z in zip(i,b):
            if(len(i)!=len(b)):
                return -1
            s=s+x*z
        d.append(s)
        s=0
    print(d)
    return d
    
        
            
            
        

    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    pass