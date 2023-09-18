import RPi.GPIO as gp
import os
import time

#actuator library and units
from zaber_motion import Library, Units
from zaber_motion.ascii import Connection

Library.enable_device_db_store()

with Connection.open_serial_port("/dev/ttyUSB0") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    #homing the actuator
    device = device_list[0]
    axis = device.get_axis(1)
    print("Resetting the actuator position")
    axis.home()
    print("Moving to the first row")
    ##The value in the command below defines how far actuator travels up to the first row of wellplates
    axis.move_relative(20, Units.LENGTH_MILLIMETRES)  

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)


def main():
    print("Starting camera A")
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    cmdA = "sudo raspistill -t 10000 -o /var/www/html/cameraA/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdA)
    ###For four more photos from the same camera
    print("Capturing the second image from camera A")
    cmdA = "sudo raspistill -t 10000 -o /var/www/html/cameraA/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdA)
    print("Capturing the third image from camera A")
    cmdA = "sudo raspistill -t 10000 -o /var/www/html/cameraA/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdA)
    print("Capturing the fourth image from camera A")
    cmdA = "sudo raspistill -t 10000 -o /var/www/html/cameraA/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdA)
    print("Capturing the fifth image from camera A")
    cmdA = "sudo raspistill -t 10000 -o /var/www/html/cameraA/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdA)
    
    print("Starting camera B")   
    i2c = "i2cset -y 1 0x70 0x00 0x05"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, False)
    gp.output(12, True)
    cmdB = "sudo raspistill -t 10000 -o /var/www/html/cameraB/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdB)
    ###For four more photos from the same camera
    print("Capturing the second image from camera B")
    cmdB = "sudo raspistill -t 10000 -o /var/www/html/cameraB/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdB)
    print("Capturing the third image from camera B")
    cmdB = "sudo raspistill -t 10000 -o /var/www/html/cameraB/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdB)
    print("Capturing the fourth image from camera B")
    cmdB = "sudo raspistill -t 10000 -o /var/www/html/cameraB/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdB)
    print("Capturing the fifth image from camera B")
    cmdB = "sudo raspistill -t 10000 -o /var/www/html/cameraB/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdB)
# #     
    print("Starting camera C")
    i2c = "i2cset -y 1 0x70 0x00 0x06"
    os.system(i2c)
    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    cmdC = "sudo raspistill -t 10000 -o /var/www/html/cameraC/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdC)
#     #For four more photos from the same camera
    print("Capturing the second image from camera C")
    cmdC = "sudo raspistill -t 10000 -o /var/www/html/cameraC/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdC)
    print("Capturing the third image from camera C")
    cmdC = "sudo raspistill -t 10000 -o /var/www/html/cameraC/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdC)
    print("Capturing the fourth image from camera C")
    cmdC = "sudo raspistill -t 10000 -o /var/www/html/cameraC/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdC)
    print("Capturing the fifth image from camera C")
    cmdC = "sudo raspistill -t 10000 -o /var/www/html/cameraC/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdC)
#     
    print("Starting camera D")
    i2c = "i2cset -y 1 0x70 0x00 0x07"
    os.system(i2c)
    gp.output(7, True)
    gp.output(11, True)
    gp.output(12, False)
    cmdD = "sudo raspistill -t 10000 -o /var/www/html/cameraD/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdD)
    #For four more photos from the same camera
    print("Capturing the second image from camera D")
    cmdD = "sudo raspistill -t 10000 -o /var/www/html/cameraD/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdD)
    print("Capturing the third image from camera D")
    cmdD = "sudo raspistill -t 10000 -o /var/www/html/cameraD/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdD)
    print("Capturing the fourth image from camera D")
    cmdD = "sudo raspistill -t 10000 -o /var/www/html/cameraD/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdD)
    print("Capturing the fifth image from camera D")
    cmdD = "sudo raspistill -t 10000 -o /var/www/html/cameraD/image%s.jpg" %time.strftime("%Y%m%d-%H%M%S")
    os.system(cmdD)
####


#i range defines how many rows you have on a transparent stage (e.g. range (0,5) means 5 rows will be imaged)
for i in range (0,2): 
    if __name__ == "__main__":
        main()
    
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)   
    if i == 1: break #No action in the last step. i should be (range-1)
    print("Waiting")
    time.sleep(0)  #waiting for 0 seconds
    print("Ready for the next round")
    #code of moving linear actuator
    with Connection.open_serial_port("/dev/ttyUSB0") as connection:
        device_list = connection.detect_devices()
        print("Moving to next row")
        device = device_list[0]
        axis = device.get_axis(1)
        axis.move_relative(135, Units.LENGTH_MILLIMETRES)
    print("Waiting to settle")
    time.sleep(1)  #waiting for 1 seconds

###     Section below is to cover the second and the third stage.
###     If your experiment does not extend to the second or the third experiment comment this part out until "Going Home" command
# print("Moving to the second stage")
# with Connection.open_serial_port("/dev/ttyUSB0") as connection:
#     device_list = connection.detect_devices()
#     device = device_list[0]
#     axis = device.get_axis(1)
#     axis.move_relative(210, Units.LENGTH_MILLIMETRES) #space between the 5th row the first stage and the first row of the second stage
# 
# 
# for i in range (0,5):    #i is the number of rows we filled with wellplates (Maximum:5) 
#     if __name__ == "__main__":
#         main()
#     
#         gp.output(7, False)
#         gp.output(11, False)
#         gp.output(12, True)   
#     if i == 4: break #No action in the last step. i should be (range-1)
#     print("Waiting")
#     time.sleep(1)  #waiting for 1 seconds
#     print("Ready for the next round")
#     #code of moving linear actuator
#     with Connection.open_serial_port("/dev/ttyUSB0") as connection:
#         device_list = connection.detect_devices()
#         print("Moving to next row")
#         device = device_list[0]
#         axis = device.get_axis(1)
#         axis.move_relative(135, Units.LENGTH_MILLIMETRES)
#     print("Waiting to settle")
#     time.sleep(1)  #waiting for 1 seconds
# 
# print("Moving to the third stage")
# with Connection.open_serial_port("/dev/ttyUSB0") as connection:
#     device_list = connection.detect_devices()
#     device = device_list[0]
#     axis = device.get_axis(1)
#     axis.move_relative(205, Units.LENGTH_MILLIMETRES)
# 
# 
# for i in range (0,4): #Maximum i range is 4 since you can fill up to 4 rows on the 3rd transparent stage
#     if __name__ == "__main__":
#         main()
#     
#         gp.output(7, False)
#         gp.output(11, False)
#         gp.output(12, True)   
#     if i == 3: break #No action in the last step. i should be (range-1)
#     print("Waiting")
#     time.sleep(1)  #waiting for 1 seconds
#     print("Ready for the next round")
#     #code of moving linear actuator
#     with Connection.open_serial_port("/dev/ttyUSB0") as connection:
#         device_list = connection.detect_devices()
#         print("Moving to next row")
#         device = device_list[0]
#         axis = device.get_axis(1)
#         axis.move_relative(135, Units.LENGTH_MILLIMETRES)
#     print("Waiting to settle")
#     time.sleep(1)  #waiting for 1 seconds

print("Going Home")
#code for taking the actuator the rest position below
with Connection.open_serial_port("/dev/ttyUSB0") as connection:
    device_list = connection.detect_devices()
    #homing the actuator
    device = device_list[0]
    axis = device.get_axis(1)
    axis.home()

print("Done")