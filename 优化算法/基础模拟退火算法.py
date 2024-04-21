# 在这个文件中，我们将实现模拟退火算法

# 为了生成随机的新解我们引入Python自带的random包
import random 
import math


# 这里是目标函数,可以自己设定,这里设定了一个简单的目标函数min(x_1^2 + 8*x_1 + x_2^2 - 16*x_2 + 32)
def setobjectivefunction(x):
    return x[0] ** 2 + 2 * x[0] + 4 * x[1] ** 2 + 32 * x[1] - 15
    # return x[0] ** 2 + 8 * x[0] + x[1] ** 2 - 16 * x[1] + 32

# 这里是模拟退火算法的主程序
# 这个函数中有6个初始参数，
# 1、objectFunction代表你需要优化的目标函数，初始为为示例目标函数,objectiveOrientation为优化方向最大化maximum还是最小化minimum
# 2、initialTemperature表示模拟退火的初始温度，finalTemperature表示模拟退火的结束温度，coolingRate表示模拟退火的降温速度，iterationRound表示模拟退火的迭代次数
# 3、initialSolution表示传入的初始解
# 这里函数的参数都给了默认值表示我们示例问题的参数
def simulatedannealing(objectiveFunction = setobjectivefunction,
                       objectiveOrientation = "minimum",
                         initialTemperature = 300, 
                         finalTemperature = 1e-8, 
                         coolingRate = 0.98, 
                         iterationRound = 100 , 
                         initialSolution = [0, 0]):
    
    # 将初始解复制给当前解
    currentSolution = initialSolution.copy()
    # 计算当前解的函数值
    currentValue = objectiveFunction(currentSolution)

    # 这里是模拟退火算法的主要程序
    while initialTemperature > finalTemperature:
            # 内部的迭代次数
            for i in range(iterationRound):
                # 随机产生新的解
                latestSolution = [ item + random.uniform(-1,1) for item in currentSolution]
                latestValue = objectiveFunction(latestSolution)

                if objectiveOrientation == "minimum":
                    # 求解最小值时的判断
                    if latestValue < currentValue:
                        currentSolution = latestSolution.copy()
                        currentValue = latestValue
                    elif math.exp((currentValue-latestValue)/initialTemperature) > (0.001 * random.randint(0,1000)):
                        currentSolution = latestSolution.copy()
                        currentValue = latestValue
                elif objectiveOrientation == "maximum":
                    # 求解最大值时的判断
                    if latestValue > currentValue:
                        currentSolution = latestSolution.copy()
                        currentValue = latestValue
                    elif math.exp(-(currentValue-latestValue)/initialTemperature) > (0.001 * random.randint(0,1000)):
                        currentSolution = latestSolution.copy()
                        currentValue = latestValue 
            # 迭代温度
            initialTemperature = initialTemperature*coolingRate

    # 得到最优解
    bestSolution = currentSolution
    bestValue = currentValue

    return bestSolution, bestValue

if __name__ == '__main__':
    bestSolution, beatValue = simulatedannealing()
    print("最优解为:")
    for i in range(len(bestSolution)):
        print(f"x{i+1}:{bestSolution[i]}")
    print(f"最优值为:{beatValue}")