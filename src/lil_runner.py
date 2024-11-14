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
BAUDRATE = 1000000                             # Baudrate of Dynamixel
DEVICENAME = '/dev/ttyUSB0'                    # Port name (adjust based on your setup, e.g., '/dev/ttyUSB0' for Linux)

# Initialize PortHandler for managing port operations, and PacketHandler for managing protocol operations
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

def tanh_controller(t):
   a = 154
   p = 0
   o = 512
   return a*math.tanh(4*math.sin(2*math.pi*(t/2 + p))) + o


# Open port
if portHandler.openPort():
   print("Port opened successfully")
else:
   print("Failed to open the port")
   quit()

# Set port baudrate 
if portHandler.setBaudRate(BAUDRATE):
   print("Baudrate set successfully")
else:
   print("Failed to set baudrate")
   quit()

start_time = time.time()

while time.time()-start_time < 10:
  # Set goal position to controller function for ankle 1
  t = time.time() - start_time
  dxl_goal_position = int(tanh_controller(t))  # (Define a goal position)
  dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ANKLE1, ADDR_MX_GOAL_POSITION, dxl_goal_position)
  if dxl_comm_result != COMM_SUCCESS:
    print(f"Error: {packetHandler.getTxRxResult(dxl_comm_result)}")
  elif dxl_error != 0:
    print(f"Error: {packetHandler.getRxPacketError(dxl_error)}")
  else:
    print(f"Goal position set to {dxl_goal_position}")

  # Set goal position to controller function for ankle 2
  t = time.time() - start_time
  dxl_goal_position = int(tanh_controller(t))  # (Define a goal position)
  dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, ANKLE2, ADDR_MX_GOAL_POSITION, dxl_goal_position)
  if dxl_comm_result != COMM_SUCCESS:
    print(f"Error: {packetHandler.getTxRxResult(dxl_comm_result)}")
  elif dxl_error != 0:
    print(f"Error: {packetHandler.getRxPacketError(dxl_error)}")
  else:
    print(f"Goal position set to {dxl_goal_position}")

  # Set goal position to controller function for knee 1
  t = time.time() - start_time
  dxl_goal_position = int(tanh_controller(t))  # (Define a goal position)
  dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, KNEE1, ADDR_MX_GOAL_POSITION, dxl_goal_position)
  if dxl_comm_result != COMM_SUCCESS:
    print(f"Error: {packetHandler.getTxRxResult(dxl_comm_result)}")
  elif dxl_error != 0:
    print(f"Error: {packetHandler.getRxPacketError(dxl_error)}")
  else:
    print(f"Goal position set to {dxl_goal_position}")

  # Set goal position to controller function for knee 2
  t = time.time() - start_time
  dxl_goal_position = int(tanh_controller(t))  # (Define a goal position)
  dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, KNEE2, ADDR_MX_GOAL_POSITION, dxl_goal_position)
  if dxl_comm_result != COMM_SUCCESS:
    print(f"Error: {packetHandler.getTxRxResult(dxl_comm_result)}")
  elif dxl_error != 0:
    print(f"Error: {packetHandler.getRxPacketError(dxl_error)}")
  else:
    print(f"Goal position set to {dxl_goal_position}")

# Close port
portHandler.closePort()
print("Port closed")