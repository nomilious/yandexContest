def gcd_fun(x, y): 
    if(y == 0): # it divide every number 
        return x  # return x 
    else: 
        return gcd_fun(y, x % y) 

a,b,c,d = map(int, input().split())

temp_m = a*d + c*b
temp_n = b*d
# наибольший общий делитель 
gcd_n = 1 if temp_m == 0 else gcd_fun(temp_m, temp_n)
print(int(temp_m/gcd_n), int(temp_n/gcd_n))
