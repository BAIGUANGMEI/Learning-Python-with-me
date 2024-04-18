# 在这个文件中，我们将实现模拟退火算法

# 这里是目标函数,可以自己设定,这里设定了一个简单的目标函数min(x_1^2 + 8*x_1 + x_2^2 - 16*x_2 + 32)
def set_objective_function(x):
    return x[0] ** 2 + 8 * x[0] + x[1] ** 2 - 16 * x[1] + 32

# 这里是模拟退火算法的主程序
def simulated_annealing(object_function = set_objective_function,
                         initial_temperature = 30, 
                         final_temperature = 1e-8, 
                         cooling_rate = 0.98, 
                         iteration_round = 100 , 
                         initial_solution = [0, 0]):
    pass


if __name__ == '__main__':
    pass