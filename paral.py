A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
C = tuple(map(int,input().split()))
print(A ,B ,C)
x4=A[0]+B[0]-C[0]
x5= A[0]+C[0]-B[0]
x6=B[0]+C[0]-A[0]
c = min(x4,x5,x6)
y4=A[1]+B[1]-C[1]
y5= A[1]+C[1]-B[1]
y6=B[1]+C[1]-A[1]
d=min(y4,y5,y6)
print(f'the coordinate is:{c,d}')