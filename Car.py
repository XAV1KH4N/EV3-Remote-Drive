class Car:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.SPEED = 1560
        
    def execute(buttons):
                
        if Button.LEFT_UP in buttons:
            self.left.run(self.SPEED)
            
        elif Button.LEFT_DOWN in buttons:
            self.left.run(-self.SPEED)

        elif Button.LEFT_UP not in buttons and Button.LEFT_DOWN not in buttons:
            self.left.brake()


        if Button.RIGHT_UP in buttons:
            self.right.run(self.SPEED)
        
        elif Button.RIGHT_DOWN in buttons:
            self.right.run(-self.SPEED)        

        elif Button.RIGHT_UP not in buttons and Button.RIGHT_DOWN not in buttons:
            self.right.brake()
            
        return Button.CENTER not in ev3.buttons.pressed()
    


        