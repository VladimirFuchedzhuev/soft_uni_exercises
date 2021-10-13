def loading_bar(n):
    ready=("%"*int(n/10))
    remain=("."*int(10-n/10))
    loading_bar = ready+remain
    return loading_bar

n = int(input())
if n==100:
    print(f'100% Complete!\n[{loading_bar(n)}]')
else:
    print(f'{n}% [{loading_bar(n)}]\nStill loading...')