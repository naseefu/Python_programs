def dogwalker():
    N,K= map(int,input().split())
    dogs=list(map(int,input('dog size:').split()))
    dogs.sort()
    diff_arr = []
    for i in range(N-1):
        diff_arr.append(dogs[i+1]-dogs[i])
    #diff_arr = [dogs[i+1]-dogs[i] for i in range(N-1)]
    diff_arr.sort(reverse=True)
    return dogs[-1]-dogs[0]-sum(diff_arr[:K-1])    

if __name__ == '__main__':
    T = int(input())
    while T:
        print(dogwalker())
        T-=1



