#### Adding spreading bullets

So you want to spruce things up a bit and allow your ship to fire in a spread (triangular) pattern.  We will look at one way to accomplish this.

First, navigate to your `bullet.py` file and find your `moveBullet` function.  We are going to modify this a bit so that if the bullet direction is up, the y position of the bullet decreases. If the direction is down, it increases.  Change your `moveBullet` function to look like the following:

        def moveBullet(self):
            if self.direction == 'up':
                self.y -= self.speed
    	    if self.direction == 'down':
    		    self.y += self.speed
            self.x += self.speed        #always move it along the x-axis
            return

Now, we need to modify the first function in that same file to receive a direction parameter.  Change your `__init__` function line to look like this:
        
        def __init__(self,width,height,x,y,color,direction='normal'):
        
Somewhere underneath that, but indented within the `__init__` function should be the following line of code:

        self.direction = direction

#### Making the spaceship actually shoot spread

Navigate to the `spaceship.py` file and find the `fire` method.  We just need to add the `direction` parameter so that when we fire, the bullet will know which direction it is supposed to travel.

Fire method inside of spaceship.py should be this:

        def fire(self,width,height,color, direction='normal'):
            return bullet.Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color, direction)
        
Finally, perhaps you could create a key binding to fire spread.  Look in the `AdventureData.py` file `evolve` function. This is what mine looks like

        if pygame.K_s in newkeys:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'up'))
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'down'))
        	
The above code would bind `spread` shooting to the `s` key.

#### Additional ideas

See that the spreading is really at a 45-degree angle.  You could perhaps tinker with the speed settings of the bullet within the `moveBullet` function to increase or decrease that angle.

Rapid fire? (Hint: change from newkeys to keys)