from pybricks.parameters import Button

class Car:
    def __init__(self, left, right, arm, ev3):
        self.ev3 = ev3
        self.arm = arm
        self.left = left
        self.right = right
        self.SPEED = 1560
        
    def execute(self,buttons):
        if Button.LEFT_DOWN in buttons and Button.LEFT_UP in buttons:
            self.arm_motor(buttons)
                                
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

    #def screen(self, buttons):
        #self.ev3.speaker.beep()
