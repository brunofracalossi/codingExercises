# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()
for i in range (0,T):
    cuts = input()
    pieces = ((cuts / 2) * (cuts / 2)) + ((cuts % 2) * (cuts / 2))
    print pieces