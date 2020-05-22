# MicroPython
Program of a EV3 Robotic Arm in MicroPython

This model sorts the blocks of different color and places them in their respective areas. The robot can carry three blocks in one maneuver and they can be placed in any order. The robot moves towards the blocks and identifies their colors with the color sensor as the blocks gets dragged into the box of the robot. When all the three blocks are captured in it, it first moves towards the specified area of the last block that was identified by the color sensor. After reaching in front of that area, it then moves back till the last block captured comes directly under the grabber. The Grabber picks up the block and places it in its area. Similarly, the robot moves to the next area and places the respective blocks.  
