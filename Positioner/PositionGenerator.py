from struct import pack

import numpy as np
import random as rd
from numpy import matlib as mt

loggInfo = 1

class DataPrepare :

    loggInfo = 1
    fileName = "trainData"

    def __init__(self, log, fileName):
        self.loggInfo = log
        self.fileName = fileName

    def classicProccessPosition(self,x0,velocity,acceleration, time):
        x = x0 + velocity*time + (acceleration * time * time )/2
        return x

    def classicProccessAllPositions(self,train_x , train_y):
        for i in range (len(train_x)):
            train_y[i][int((self.classicProccessPosition(train_x[i][0],train_x[i][1],train_x[i][2],train_x[i][3])))] = 1


    def randomizeParam(self):
        paramMap = {"x0": 0 , "velocity" : 0 , "acceleration" : 0 , "time" : 0}
        paramMap["x0"]              = rd.uniform(1,10)
        paramMap["velocity"]        = rd.uniform(1, 10)
        paramMap["acceleration"]    = rd.uniform(1, 10)
        paramMap["time"]            = rd.uniform(1, 10)
        if loggInfo : print paramMap
        return paramMap

    def logTraiData(self,train_x, train_y):
        for i in range(len(train_x)):
            print "x: " + str(train_x[i]) + " y: " + str(train_y[i])

    def putGeneratedDataToVectors(self,train_x):
        for x in train_x :
            paramMap = self.randomizeParam()
            x[0] = paramMap["x0"]
            x[1] = paramMap["velocity"]
            x[2] = paramMap["acceleration"]
            x[3] = paramMap["time"]

    def generateTrainDataToFile(self,fileName):
        train_x = np.zeros((100,4))
        train_y = np.zeros((100,700))

        self.putGeneratedDataToVectors(train_x)

        if loggInfo:
            print "=================================================================================="

        if loggInfo:
            self.logTraiData(train_x,train_y)

        if loggInfo:
            print "=================================================================================="
        self.classicProccessAllPositions(train_x , train_y)
        if loggInfo:
            self.logTraiData(train_x,train_y)

dp = DataPrepare(1,"data")
dp.generateTrainDataToFile("data")