class Solution(object):
    def mySqrt(self, x):
        if x==0:return 0
        a=1
        while True:
            pre=a
            a=1/2*(a+x/a)
            if abs(a-pre)<1:
                return int(a)

if __name__ == '__main__':
    x=8

    sol=Solution()
    ans=sol.mySqrt(x)
    print(ans)