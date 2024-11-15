import os
import time
from dynamixel_sdk import *                    # Uses the Dynamixel SDK library
import math
 
# Control table address for AX-18 (Protocol 1.0)
ADDR_MX_LED = 25                               # LED address
ADDR_MX_GOAL_POSITION = 30                     # Goal position address
ADDR_MX_PRESENT_POSITION = 36                  # Present position address

# Protocol version (for AX-18, AX-12, it's 1.0)
PROTOCOL_VERSION = 1.0                        

# Default settings
ANKLE1 = 1
ANKLE2 = 6   
KNEE1 = 2
KNEE2 = 5  
HIP1 = 3
HIP2 = 4        
all_joint_ids = [ANKLE1, ANKLE2, KNEE1, KNEE2, HIP1, HIP2]               
BAUDRATE = 1000000                             # Baudrate of Dynamixel
DEVICENAME = '/dev/ttyUSB0'                    # Port name (adjust based on your setup, e.g., '/dev/ttyUSB0' for Linux)

# Initialize PortHandler for managing port operations, and PacketHandler for managing protocol operations
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def sin_controller(t: float, a: int=154, p: int=0) -> int:
  '''
    input: t (time), a (amplitude), p (phase)
    output: angle of joint given the time, amplitude and phase
  '''

  o: int = 512
  #return int(a*math.tanh(4*math.sin(2*math.pi*(t/2 + p))) + o)
  return int(a*math.sin(6*t+p) + o)

def set_goal_position(joint_id: int, dxl_goal_position: int)  -> None:
  '''
  input: 
    joint_id: id of a desired dynamixel, 
    dxl_goal_position: desired angle for dynamixel

  output: 
    None, but sets the angle of dynamixel to dxl_goal_position
  '''
  dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, joint_id, ADDR_MX_GOAL_POSITION, dxl_goal_position)
  if dxl_comm_result != COMM_SUCCESS:
    print(f"Error: {packetHandler.getTxRxResult(dxl_comm_result)}")
  elif dxl_error != 0:
    print(f"Error: {packetHandler.getRxPacketError(dxl_error)}")
  else:
    print(f"Goal position set to {dxl_goal_position}")


# Open port
if portHandler.openPort():
   print("Port opened successfully")
else:
   print("Failed to open the port")
   quit()

# initialize angles
for joint in all_joint_ids:
  set_goal_position(joint, 512)

time.sleep(1)

# Set port baudrate 
if portHandler.setBaudRate(BAUDRATE):
   print("Baudrate set successfully")
else:
   print("Failed to set baudrate")
   quit()

joint_ids = [ANKLE1, ANKLE2,KNEE1, KNEE2, HIP1]
start_time = time.time()
while time.time()-start_time < 10:

  t = time.time() - start_time
  goal_angle = sin_controller(t)  # (Define a goal position)
  hip2_angle = sin_controller(t, p=math.pi)

  for joint in joint_ids:
    set_goal_position(joint, goal_angle) 

  # due to the assembly of robot, hip4 needs to be phased to mirror the other hip
  set_goal_position(HIP2, hip2_angle)

# initialize angles
for joint in all_joint_ids:
  set_goal_position(joint, 512)

# Close port
portHandler.closePort()
print("Port closed")