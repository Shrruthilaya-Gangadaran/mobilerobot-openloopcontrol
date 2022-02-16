from robomaster import robot
import time
from robomaster import camera

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    
    ep_chassis = ep_robot.chassis
    ep_camera = ep_robot.camera
    ep_led = ep_robot.led
    
    '''
    x = x-axis movement distance,( meters) [-5,5]
    y = y-axis movement distance,( meters) [-5,5]
    z = rotation about z axis ( degree)[-180,180]
    xy_speed = xy axis movement speed,( unit meter/second) [0.5,2]
    '''
    print("Camera streaming started...")
    ep_camera.start_video_stream(display=True, resolution=camera.STREAM_360P) 

    ep_chassis.move(x=1, y=0, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=0,g=255,b=0,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=0, y=1, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=255,g=0,b=0,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=1.5, y=0, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=0,g=0,b=255,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=0, y=0, z=90, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=255,g=0,b=0,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=2, y=0, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=0,g=255,b=0,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=0, y=0, z=90, xy_speed=0.75).wait_for_completed()
    
    ep_led.set_led(comp="all",r=0,g=0,b=255,effect="on")
    time.sleep(2)
    
    ep_chassis.move(x=2.5, y=0, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_camera.stop_video_stream()
    
    print("Stopped video streaming...")
    ep_robot.close()