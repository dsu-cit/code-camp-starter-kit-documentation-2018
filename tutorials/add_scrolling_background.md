#### Adding a scrolling background

Our game will be much more interesting if we can make it look like a 2d side-scrolling game, to make it seem as if the ship is really navigating through space. 

Essentially, this will entail setting a background image for our game, but instead of it remaining static, we will make it move to the left.  Another key concept, is that in order for this image to last for the duration of the game, we will create a flipped copy of the image and as soon as the first image goes off the side of the screen, we will display the next image.  We will keep rotating in this fashion forever.

#### Adding a background class

We will first make a class called `Background` which will allow us to move the images easier.  Start by creating a new file called `background.py`, save it in the directory of your game.

Create the following class definition:

        class Background( pygame.sprite.Sprite ):
            def __init__( self, filename, width ):
                pygame.sprite.Sprite.__init__( self )   #becomes a sprite
                self.screen_width = width               #store screen width
                image = pygame.image.load( filename )   #load the image
                image = image.convert( )
                self.rect = image.get_rect( )
                self.image = image
                self.flipped_image = pygame.transform.flip( self.image, 1, 0 ) #flip the image
                self.flipped_rect = self.flipped_image.get_rect( )
                self.flipped_rect.left = self.rect.right #set the starting point of the second image                
                self.dx = -5	    #this will control how fast the background moves

Note how in the above code, we start the flipped_images rectangle to be at the right hand side of the normal image.

#### Draw the background

We need to create a method that will allow us to draw the background. This will go in the same file. Make sure you have it properly indented so it is within the `Background` class.

        def draw( self, surface ):
            surface.blit( self.image, self.rect )
            surface.blit( self.flipped_image, self.flipped_rect )


#### Handle movement of the background

Remember that each frame of the game we want to move the background image to the left. (You could have it move other directions if you want, but left is the most natural).  Here is the logic:

- Move the (main image) rectangle and the flipped rectangle to the left by adding `self.dx` to the current left position of each.
- When the (main image) rectangle's right side goes off the left side of the screen, move it to the end of the flipped rectangle.
- Do the same thing as the previous step when the flipped rectangle goes off the screen.

To implement this in code, I would create a method (still inside the `Background` class) that is called `update`:

        def update( self ):
            self.rect.left +=self.dx
            self.flipped_rect.left +=self.dx
            if self.rect.right < 0:
                    self.rect.left = self.flipped_rect.right

            if self.flipped_rect.right<0:
                    self.flipped_rect.left = self.rect.right

Save your file (`background.py`).

#### Tying it all together

Well, you have a class, but it isn't much good unless you add it to your game.  At the top of `game_program.py`, you should add a line which will import your newly created code.

        import background

Now look for your `__init__` method inside of `GameProgram`.  You need to create an instance of your background.  Somewhere in that `__init__` method add the following line:
     
        self.bg = background.Background( 'background.jpg', width )
        
Note that we are expecting that you have a file called `background.jpg` in your project directory.  `width` refers to the width of the screen.

Find the `evolve()` method inside of `GameProgram`, at the very first line of that you should add a call to your background update method:

        self.bg.update()


Finally, we need to tell the `GameProgram` draw method to call the `draw()` method of your background.  You can do this by searching for the following line of code within the draw method:

        surface.fill( ( 0, 0, 0 ), rect )

And right after it, add the following line:

        self.bg.draw( surface )

You have to make sure that you draw your background first or you won't see your ship!  Run your code and you should have a scrolling background.

#### Optional fun

You could tie the speed of your background to some sort of user control.  For example, if the user were to press the `w` key for warp-speed, you could make the `dx` variable of your `Background` class increase.
