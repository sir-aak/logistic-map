import numpy as np
import matplotlib.pyplot as plt


r = 3.8


def logisticMapStep (x):
    return (r * x * (1.0 - x))


def makeTimeSeries (x0=0.1, nSteps=10000, tSteps=9900):
    
    global r
    
    # initial condition
    x = x0
    
    X = np.zeros(nSteps)
    T = np.arange(start=0, stop=nSteps)
    
    # write initial condition into time series vector
    X[0] = x
    
    for i in np.arange(start=1, stop=nSteps):
        x    = logisticMapStep(x)
        X[i] = x
    
    return (T[tSteps:], X[tSteps:])


def plotTimeSeries ():
    
    T, X = makeTimeSeries()
    
    plt.figure(figsize=(5.9, 3.8))
    plt.subplots_adjust(top=0.97, bottom=0.17, left=0.14, right=0.95)
    plt.plot(T, X)
    plt.ylim(0.0, 1.0)
    plt.xlabel("steps")
    plt.ylabel("relative population")
    plt.grid(color="lightgray")
    plt.show()


def isExtremum (xprev, x, xnext):
    
    if (x > xprev and x > xnext):
        return (True)
    
    elif (x < xprev and x < xnext):
        return (True)
    
    else:
        return (False)


def plotBifurcationDiagram (zoom = False):
    
    myfontsize = 18.0
    
    global r
    
    if zoom == False:
        RList = np.arange(start=0.0, stop=4.0 + 1e-10, step=0.001)
    
    if zoom == True:
        RList = np.arange(start=2.85, stop=4.0 + 1e-10, step=0.0005)
    
    extremaList = []
    
    exList = []
    rList  = []
    
    for R in RList:
        
        r    = R
        T, X = makeTimeSeries()
        
        for i in range(1, len(X[:-2])):
            
            x = X[i]
            
            if (isExtremum(X[i-1], x, X[i+1]) == True):
                extremaList.append(x)
            
            i += 1
        
        # non-oscillating solution
        if extremaList == []:
            rList.append(r)
            exList.append(X[-1])
        
        # oscillating solution
        for extremum in extremaList:
            rList.append(r)
            exList.append(extremum)
        
        extremaList = []
        
        print(np.around(100.0 * r / RList[-1], 2), " %")
        
    print("number of data points: ", len(exList))
    
    plt.figure(figsize=(5.9, 4.5))
    plt.subplots_adjust(top=0.98, bottom=0.17, left=0.15, right=0.98)
    plt.scatter(rList, exList, color="black", marker=".", s=0.01, zorder=2)
    plt.xlabel(r"bifurcation parameter $r$", fontsize=myfontsize)
    plt.ylabel(r"extrema $\hat{x}$", fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)
    
    if zoom == False:
        plt.xticks([0.0, 1.0, 2.0, 3.0, 4.0], fontsize=myfontsize)
        plt.xlim(-0.075, 4.075)
    
    if zoom == True:
        plt.xticks([3.0, 3.25, 3.5, 3.75, 4.0], ["3.0", "3.25", "3.5", "3.75", "4.0"], fontsize=myfontsize)
        plt.xlim(2.875, 4.025)
    
    plt.ylim(-0.025, 1.025)
    plt.grid(color="lightgray")
    plt.show()


plotTimeSeries()
plotBifurcationDiagram(zoom=False)
