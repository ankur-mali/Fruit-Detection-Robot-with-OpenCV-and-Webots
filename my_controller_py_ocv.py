import cv2
import numpy as np
from controller import Supervisor, DistanceSensor, PositionSensor, Camera, Motor

TIME_STEP = 32

WAITING, PICKING, ROTATING, DROPPING, ROTATE_BACK = range(5)

def process_image_with_opencv(image_data, width, height):
    # Convert the image from Webots format (BGRA) to OpenCV format (BGR)
    img = np.frombuffer(image_data, np.uint8).reshape((height, width, 4))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    
    # Example OpenCV processing: Convert to grayscale and detect edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    
    # Display the processed image using OpenCV (optional, for debugging)
    cv2.imshow("Edges", edges)
    cv2.waitKey(1)
    
    # You can add more image processing logic here
    # Return any results that might be useful for your robot
    return edges

def main():
    supervisor = Supervisor()
    
    counter = 0
    state = WAITING
    target_positions = [-1.570796, -1.87972, -2.139774, -2.363176, -1.50971]
    
    speed = 2.0
    model = 0
    fruit = ''
    apple = 0
    orange = 0

    # Getting and declaring the 3 finger motors of the gripper 
    hand_motors = []
    hand_motors.append(supervisor.getDevice("finger_1_joint_1"))
    hand_motors.append(supervisor.getDevice("finger_2_joint_1"))
    hand_motors.append(supervisor.getDevice("finger_middle_joint_1"))

    # Getting and declaring the robot motor
    ur_motors = []
    ur_motors.append(supervisor.getDevice("shoulder_pan_joint"))
    ur_motors.append(supervisor.getDevice("shoulder_lift_joint"))
    ur_motors.append(supervisor.getDevice("elbow_joint"))
    ur_motors.append(supervisor.getDevice("wrist_1_joint"))
    ur_motors.append(supervisor.getDevice("wrist_2_joint"))

    # Declaring and enabling the camera for recognitions
    camera = supervisor.getDevice("camera")
    camera.enable(2 * TIME_STEP)
    camera.recognitionEnable(2 * TIME_STEP)
    
    for motor in ur_motors:
        motor.setVelocity(speed)

    distance_sensor = supervisor.getDevice("distance sensor")
    distance_sensor.enable(TIME_STEP)

    position_sensor = supervisor.getDevice("wrist_1_joint_sensor")
    position_sensor.enable(TIME_STEP)

    # Main loop
    while supervisor.step(TIME_STEP) != -1:
        # Get the camera image
        image_data = camera.getImage()
        width = camera.getWidth()
        height = camera.getHeight()
        
        # Process the image with OpenCV
        edges = process_image_with_opencv(image_data, width, height)
        
        # Get the camera object recognition details
        number_of_objects = camera.getRecognitionNumberOfObjects()
        
        # Get and display the objects information
        objects = camera.getRecognitionObjects()

        if number_of_objects > 0:
            fruit = objects[0].getModel()
            if fruit[0] == 'a':  # ASCII value of 'a' is 97
                model = 1
            else:
                model = 0

        # Switch cases for the different state of the arm
        if counter <= 0:
            if state == WAITING:
                if distance_sensor.getValue() < 500:
                    state = PICKING
                    if model == 1:
                        apple += 1
                    else:
                        orange += 1
                    counter = 8
                    for motor in hand_motors:
                        motor.setPosition(0.52)
            elif state == PICKING:
                for i in range(model, 5):
                    ur_motors[i].setPosition(target_positions[i])
                state = ROTATING
            elif state == ROTATING:
                if position_sensor.getValue() < -2.3:
                    counter = 8
                    state = DROPPING
                    for motor in hand_motors:
                        motor.setPosition(motor.getMinPosition())
            elif state == DROPPING:
                for i in range(model, 5):
                    ur_motors[i].setPosition(0.0)
                state = ROTATE_BACK
            elif state == ROTATE_BACK:
                if position_sensor.getValue() > -0.1:
                    state = WAITING
        
        counter -= 1

        strP = f"Oranges: {orange}"
        supervisor.setLabel(0, strP, 0.45, 0.96, 0.06, 0x5555ff, 0, "Lucida Console")
        
        strP = f"Apples: {apple}"
        supervisor.setLabel(1, strP, 0.3, 0.96, 0.06, 0x5555ff, 0, "Lucida Console")

    supervisor.cleanup()

if __name__ == "__main__":
    main()
