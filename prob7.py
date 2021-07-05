from matplotlib import pyplot as plt
from numba import njit
import matplotlib.animation as animation
import numpy as np
from random import random

LENGTH = 100
numTimeSteps = 10**3


@njit
def function():
    timeSteps = [[(random()*150)+30 for i in range(LENGTH)]]
    coeff = 0.8
    coeff2 = 1-coeff

    for iter in range(numTimeSteps-1):
        timeSteps.append([float(x) for x in range(0)])
        for i in range(LENGTH):
            if i == 0:
                timeSteps[-1].append(round(timeSteps[iter][i]*coeff, 2))
            else:
                timeSteps[-1].append(round(timeSteps[iter][i]*coeff + coeff2*timeSteps[iter][i-1], 2))

    return timeSteps


def main():
    pastTraf = [20]+[0]*19
    
    #Creating the dataset
    for t in range(19):
        traf=[]
        for i,data in enumerate(pastTraf):
            # For the 1st element in the list
            if not i:
                traf.append(data *0.9)
                continue
            # For the last element in the list
            elif i == len(pastTraf)-1:
                traf.append(0.1*pastTraf[i-1]+data*0.9)
                continue
            #For the intermediate elements
            traf.append(0.9*data+0.1*pastTraf[i-1])

        # pastTraf = list(map(round,traf))
        # Takes out negatives
        accumulatedData = list(map(isNeg,traf))
        print(type(accumulatedData))
        data_points = accumulatedData[0]
        # indices, data = enumerate(accumulatedData[0])
        

        if len(pastTraf)>20:
            break

def speed(density):
    if density <= 30:
        return 60
    elif density >=150:
        return 0
    return 75-(density/2)


if __name__=='__main__':
    funct = function()
    data = []
    [data.append(list(map(speed,f))) for f in funct]
    data = np.array(data)
    indices=np.array([i for i in range(LENGTH)])
    
    # print(data)

    # [print(thing) for thing in data]
    fig, ax = plt.subplots()

    line, = ax.plot(indices, data[0])
    
    def animate(i):
        try:
            line.set_ydata(data[i])
        except:
            pass
        return line,


    ani = animation.FuncAnimation(
        fig,animate,interval=30,blit=True,save_count=50
    )
    plt.ylim([0,61])
    plt.show()
    # print(type(line))
