from pybricks.parameters import Button
from pybricks.media.ev3dev import SoundFile, ImageFile

class Car:
    def __init__(self, left, right, arm, infra, ev3):
        self.ev3 = ev3
        self.arm = arm
        self.left = left
        self.right = right
        self.infra = infra
        self.SPEED = 1560
        self.TURN_90 = 630
        
    def autorun(self):
        while Button.CENTER not in self.ev3.buttons.pressed():
            distance = self.infra.distance()
            
            buttons = self.infra.keypad()
            
            if Button.LEFT_UP in buttons:
                self.rotate(-self.TURN_90)
                
            elif Button.RIGHT_UP in buttons:
                self.rotate(self.TURN_90)
                

                
                        
    def rotate(self, angle):
        self.left.run_angle(self.SPEED, angle, wait=False)
        self.right.run_angle(self.SPEED, -angle)
        
    def execute(self,buttons):
        if Button.LEFT_DOWN in buttons and Button.LEFT_UP in buttons:
            self.arm_motor(buttons)
            
        elif Button.RIGHT_DOWN in buttons and Button.RIGHT_UP in buttons:
            self.screen(buttons)
                                
        else:    
            self.left_motor(buttons)
            self.right_motor(buttons)
            
        return Button.CENTER not in self.ev3.buttons.pressed()
    
    def right_motor(self, buttons):
        if Button.RIGHT_UP in buttons:
            self.right.run(self.SPEED)
            
        elif Button.RIGHT_DOWN in buttons:
            self.right.run(-self.SPEED)        

        elif Button.RIGHT_UP not in buttons and Button.RIGHT_DOWN not in buttons:
            self.right.brake()
    
    def left_motor(self, buttons):
        if Button.LEFT_DOWN in buttons:
                self.left.run(-self.SPEED)
                
        if Button.LEFT_UP in buttons:
            self.left.run(self.SPEED)

        elif Button.LEFT_UP not in buttons and Button.LEFT_DOWN not in buttons:
            self.left.brake()
            self.arm.brake()
    
    
    def arm_motor(self, buttons):
        self.left.brake()
        self.right.brake()
                               
        if Button.RIGHT_UP in buttons:
            self.arm.run(-self.SPEED)
                
        elif Button.RIGHT_DOWN in buttons:
            self.arm.run(self.SPEED)
                
        else:
            self.arm.brake()

    def screen(self, buttons):
        if Button.LEFT_UP in buttons:
            self.ev3.speaker.play_file(SoundFile.BOING)
        
        elif Button.LEFT_DOWN in buttons:
            self.ev3.speaker.play_file(SoundFile.CONFIRM)
