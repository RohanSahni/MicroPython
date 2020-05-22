#!/usr/bin/env pybricks-micropython
 
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
# Configure the grabber motor on Port A with default settings.
# Initialize a motor where positive speed values should go clockwise
grabber= Motor(Port.A, Direction.CLOCKWISE,[4,4])
# Configure the arm motor. It has an 8-teeth and a 40-teeth gear
# connected to it. We would like positive speed values to make the
# arm go upward. This corresponds to clockwise rotation
# of the motor.
arm=Motor(Port.D, Direction.CLOCKWISE, [8, 40])# Configure the motor that rotates the base.
base_motor_B = Motor(Port.B)
base_motor_C = Motor(Port.C)
# Limit the arm and base accelerations. This results in
# very smooth motion. Like an industrial robot.
arm.set_run_settings(60, 120)
base_motor_B.set_run_settings(60, 120)
base_motor_C.set_run_settings(60,120)
wheels= DriveBase(base_motor_B,base_motor_C,56,114)
 
# The colored objects are either red, green, blue, or yellow.
POSSIBLE_COLORS = (Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW)
# Initialize the color sensor
color_sensor= ColorSensor(Port.S4)
 
# Initialize the arm. First make it go down for one second.
# Then make it go upwards slowly (15 degrees per second) until
# a brick button is pressed. Then reset the motor
# angle to make this the zero point. Finally, hold the motor
# in place so it does not move.
arm.run_time(-30, 1000)
arm.run_time(15,1000)
while not brick.buttons():
   wait(10)  
arm.reset_angle(0)
arm.stop(Stop.HOLD)
# Initialize the base. First move it until the brick button
# in the base is pressed. Reset the motor angle to make this
# the zero point. Then hold the motor in place so it does not move.
wheels.drive_time(60,0,2000)
while not (brick.buttons()):
   wait(10)
base_motor_B.reset_angle(0)
base_motor_C.reset_angle(0)
base_motor_B.stop(Stop.HOLD)
base_motor_C.stop(Stop.HOLD)
# Initialize the grabber. First rotate the motor until it stalls.
# Stalling means that it cannot move any further. This position
# corresponds to the closed position. Then rotate the motor
# by -90 degrees such that the gripper is open.
grabber.run_until_stalled(200, Stop.COAST, 50)
grabber.reset_angle(0)
grabber.run_target(200, -90)
###############################################################################
#define the path to area of each block 
 
def area(color):
   if color==Color.RED:
       wheels.drive_time(-60,0,2000)
       wheels.drive(-100,90)
       wheels.drive_time(-60,0,2000)
   elif color==Color.BLUE:
       wheels.drive_time(60,0,2000)
       wheels.drive(-60,90)
       wheels.drive_time(-60,0,2000)
   elif color==Color.YELLOW:
       wheels.drive(-60,-90)
       wheels.drive_time(-60,0,2000)
   elif color==Color.GREEN:
       wheels.drive(60,90)
       wheels.drive_time(-60,0,2000)
   else:
       wheels.drive_time(-60,4000)
       wheels.drive_time(60,1000)
       wheels.drive(-60,360)
   return(color)
 
#this is the main function of the program. It moves to the specified area of the block and then places them accordingly.
def block_area(first_color,second_color,third_color):
   if first_color == Color.BLUE:
       area(Color.BLUE)
   elif first_color == Color.GREEN:
       area(Color.GREEN)
   elif first_color == Color.YELLOW:
       area(Color.YELLOW)
   elif first_color == Color.RED:
       area(Color.RED)
   wheels.drive_time(30,0,2000)
   # Lower the arm.
   arm.run_target(60, -40)
   # Close the grabber to grab the block.
   grabber.run_until_stalled(200, Stop.HOLD, 50)
   # Raise the arm to lift the block.
   arm.run_target(60, 0, Stop.HOLD)
   wheels.drive_time(-30,0,2000)
   # Lower the arm to place the block.
   arm.run_target(60, -40)
   # Open the grabber to release the block.
   grabber.run_angle(-200,90)
   #grabber.run_until_stalled(-200, Stop.HOLD, 50)
   #Raise the arm
   arm.run_target(60,   0, Stop.HOLD)
   #Move to reference line
   wheels.drive_time(60,0,2000)
 
   # Second area
   if color == Color.BLUE:
       area(Color.BLUE)
   elif color == Color.GREEN:
       area(Color.GREEN)
   elif color == Color.YELLOW:
       area(Color.YELLOW)
   elif color == Color.RED:
       area(Color.RED)
   wheels.drive_time(30,0,2000)
   arm.run_target(60, -40)
   grabber.run_until_stalled(200, Stop.HOLD, 50)
   arm.run_target(60, 0, Stop.HOLD)
   wheels.drive_time(-30,0,2000)
   # Lower the arm to place the block.
   arm.run_target(60, -40)
   # Open the gripper to release the block.
   grabber.run_angle(-200,90)
   #grabber.run_until_stalled(-200, Stop.HOLD, 50)
   #Raise the arm
   arm.run_target(60, 0, Stop.HOLD)
   #Move to reference line
   wheels.drive_time(60,0,2000)
  
 
   # Third area
   if color == Color.BLUE:
       area(Color.BLUE)
   elif color == Color.GREEN:
       area(Color.GREEN)
   elif color == Color.YELLOW:
       area(Color.YELLOW)
   elif color == Color.RED:
       area(Color.RED)
   wheels.drive_time(30,0,2000)
   arm.run_target(60, -40)
   grabber.run_until_stalled(200, Stop.HOLD, 50)
   arm.run_target(60, 0, Stop.HOLD)
   wheels.drive_time(-30,0,2000)
   # Lower the arm to place the block.
   arm.run_target(60, -40)
   # Open the grabber to release the block.
   grabber.run_angle(-200,90)
   #grabber.run_until_stalled(-200, Stop.HOLD, 50)
   #Raise the arm
   arm.run_target(60, 0, Stop.HOLD)
   #Move to reference line
   wheels.drive_time(60,0,2000)
 
##################################################################################
color_list=[]
while len(color_list)!=3:
   # Store the color measured by the Color Sensor.
   color = color_sensor.color()
   wait(1000)
   if color in POSSIBLE_COLORS:
#add Colors to the list       color_list.append(color_sensor.color())
       wheels.drive_time(-60,0,2000)
   else:
       wheels.drive_time(-60,0,3000)
print(color_list)
# Wait for one second 
wait(1000)
# Assign first, second and third color to the Colors stored in the list.
first_color=color_list[2]
second_color=color_list[1]
third_color=color_list[0]
#Then run the main function
block_area(first_color, second_color, third_color)
# Play three beeps to indicate that one maneuver is complete.
brick.sound.beeps(3)
