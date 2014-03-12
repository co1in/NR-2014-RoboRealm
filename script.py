import rr
import math

leftDiffX = int(rr.GetVariable("TopLeftX")) - int(rr.GetVariable("BottomLeftX"))
leftDiffY = int(rr.GetVariable("TopLeftY")) - int(rr.GetVariable("BottomLeftY"))
rightDiffX = int(rr.GetVariable("TopRightX")) - int(rr.GetVariable("BottomLeftX"))
rightDiffY = int(rr.GetVariable("TopRightY")) - int(rr.GetVariable("BottomRightY"))

d1 = (leftDiffX**2 + leftDiffY**2)**0.5
d2 = (rightDiffX**2 + rightDiffY**2)**0.5

rr.SetVariable("AVERAGE_HEIGHT", ((float(d1)+float(d2))/float(2)))
