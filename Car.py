from pybricks.parameters import Button

class Car:
    def __init__(self, left, right, arm, ev3):
        self.ev3 = ev3
        self.arm = arm
        self.left = left
        self.right = right
        self.SPEED = 1560
        
    def execute(self,buttons):
        if Button.BEACON in buttons:
            pass
        if Button.LEFT_UP in buttons:
            self.left.run(self.SPEED)
            #self.arm.run_target(800,-1080)
            
        elif Button.LEFT_DOWN in buttons:
            self.left.run(-self.SPEED)
            #self.arm.run_target(800,1080)

        elif Button.LEFT_UP not in buttons and Button.LEFT_DOWN not in buttons:
            self.left.brake()

        if Button.RIGHT_UP in buttons:
            self.right.run(self.SPEED)
        
        elif Button.RIGHT_DOWN in buttons:
            self.right.run(-self.SPEED)        

        elif Button.RIGHT_UP not in buttons and Button.RIGHT_DOWN not in buttons:
            self.right.brake()
            
        return Button.CENTER not in self.ev3.buttons.pressed()
    


        