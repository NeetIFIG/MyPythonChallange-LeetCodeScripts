# Day 1 - 30DaysOfPython Challenge
import sys
import math
def wildFUntion(a):
    print (type(a))

def CalculateEcluideanDis(pointA,PointB):
    a = (pointA[0]-PointB[0])**2+(pointA[1]-PointB[1])**2
    dis = math.sqrt(a)
    return dis

def ReturnIntAfterAsk(CoordenateToAsk):
    temp = input("Enter " + CoordenateToAsk+" : ")
    if(temp.isnumeric()):
        num = float(temp)
        return num
    else:
        print("Non Valid Coordenate")

print(sys.version)

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print("Im not saying my name")
print("I'm bad at leetcode")

print ("Her's some data types")

wildFUntion(234)
wildFUntion(0.25)
wildFUntion(5+6j)
wildFUntion("NOthing Here")
wildFUntion(False)
wildFUntion(["Super","List","Of","String"])
wildFUntion((3,4,2,1,2,3,"Tuple"))
wildFUntion({"There","is","No","Order","Here"})
wildFUntion({"KeyDic":1,"KeyDic2":2,"KeyDic3":3,"KeyDic4":4})

b=CalculateEcluideanDis((2,3),(10,8))
print(b)
Point1 = (ReturnIntAfterAsk("X1"),ReturnIntAfterAsk("Y1"))
Point2 = (ReturnIntAfterAsk("X2"),ReturnIntAfterAsk("Y2"))
c=CalculateEcluideanDis(Point1,Point2)
print(c)