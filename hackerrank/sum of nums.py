# Enter your code here. Read input from STDIN. Print output to STDOUT


def main():
    n = int(input())
    sum = 0
    
    for i in range(n):
        num = int(input().strip())
        sum += num
    print(sum)

main()