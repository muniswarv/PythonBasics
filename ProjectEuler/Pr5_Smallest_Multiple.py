
def pr5_smallest_multiple(n):
    
    out = 1
    while(True):
        if not [ False for i in range(1, n+1) if out%i != 0 ]: return out
        out += 1
        if out%100 == 0: print(out)
        
    return None
        
print( " 10 => ",  pr5_smallest_multiple(10) )
print( " 20 => ",  pr5_smallest_multiple(20) )


