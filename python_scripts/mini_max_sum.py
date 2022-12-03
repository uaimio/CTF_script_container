def miniMaxSum(arr):
    max_sum = 0
    min_sum = 10000000000
    
    for i in range(5):
        if i < 4:
            temp = sum(arr[:i] + arr[i+1:])
        else:
            temp = sum(arr[:i])
            
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp
                
    print(f'{min_sum} {max_sum}')
    

if __name__ == '__main__':

    arr = [769082435, 210437958, 673982045, 375809214, 380564127]

    miniMaxSum(arr)
