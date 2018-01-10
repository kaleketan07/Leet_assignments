# This is analogous to the Fibonacci series
# the number of ways in which one can climb n steps is the nth term in the fibonacci sequence starting from 1

ways = {'1': 1,
        '2': 2}
def climbStairs(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if str(n) in ways.keys():
            print ways[str(n)]
            return ways[str(n)]
        else:
            ways[str(n)] = climbStairs(n - 1) + climbStairs(n - 2)
            print ways[str(n)]
            return ways[str(n)]





if __name__ == '__main__':
    climbStairs(5)


