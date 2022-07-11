import bpy
import os
import threading
import time
import sys


bone3 = bpy.data.objects["Armature"].pose.bones['Tentacle.sec3.IK']
bone2 = bpy.data.objects["Armature"].pose.bones['Tentacle.sec2.IK']
bone1 = bpy.data.objects["Armature"].pose.bones['Tentacle.sec1.IK']

def reset():
    bone1.location = (0,0,0)
    bone2.location = (0,0,0)
    bone3.location = (0,0,0)
    
def CreateTest(X,Y,Z):    # creates a test file with input coords
    with open('BlenderProject/test.txt', 'w') as f:
        print(X,file=f)
        print(Y,file=f)
        print(Z,file=f)
        f.close()
    
def OutputTest(X,Y,Z):      # creates output file with input coords
    with open('BlenderProject/OutputTest.txt', 'w') as f:
        print(X,file=f)
        print(Y,file=f)
        print(Z,file=f)
        f.close()
        
def GetFinalp():
    X = 0; Y = 0; Z = 0     # runs the test file for generated input
    with open('BlenderProject/OutputTest.txt', 'r') as f:
        X = float(f.readline())
        Y = float(f.readline())
        Z = float(f.readline())
        f.close()
    return [X,Y,Z]
    
    
def RunTestFile():
    X = 0; Y = 0; Z = 0     # runs the test file for generated input
    with open('BlenderProject/test.txt', 'r') as f:
        while f: 
            X = f.readline()
            if (X == ""):
                break
            X = float(X)
            Y = float(f.readline())
            Z = float(f.readline())
            bone3.location = (X,Y,Z)
        f.close()
