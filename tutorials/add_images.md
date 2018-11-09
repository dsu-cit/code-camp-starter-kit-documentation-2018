Replacing Rectangles with Images
--------------------------------

I'm going to add a baddie picture to my game, instead of 
drawing a red rectangle.

Image Files
-----------

First, I need to make or find the image file.  There are many
image file formats.  Pygame supports many of them, but it depends
on your computer system installation.  It's best to convert to
`.png` or `.jpg`.

I created and image file: `baddie.png`.


Loading Image Files
-------------------

Next, we'll need to load the image file into the program
so we can display it when we want to draw a baddie.  
This needs to be completed in `GameProgram`'s `__init__` method.  Here
are the lines I would put.

    self.baddie_image = pygame.image.load( "baddie.png" )

Notice the name of the image file is in quotes.  The
name must match the file name exactly.  If your operating
system hides the file extension, be sure that you have it
correct.

You should check your program for syntax errors before proceeding.


Give the Image to the Baddies
----------------------------

Now that the image is loaded into the program, we need to
make it part of every baddie.  I went to the `addBaddie`
method of `GameProgram` and found the line:

    new_baddie = baddie.Baddie( self.baddie_width, self.baddie_height, x, y, self.baddie_color )
    
Add the baddie image to it.

    new_baddie = baddie.Baddie( self.baddie_width, self.baddie_height, x, y, self.baddie_color, self.baddie_image )
    
This will send the image to every newly created baddie.  The baddie needs to 
know that it has an image.  We add to `Baddie`'s `__init__` method.  First, 
let it know that there is an image:

    def __init__( self, width, height, x, y, color, image ):

Then, tell it to store the image by adding this line:

        self.image = image
        
        
Show the Image
--------------

To make the rectangle not draw, and make the image show up, we go to
the `draw` method of `Baddie`.  Remove this line:

        pygame.draw.rect( surface, self.color, rect )

Add this line in its place:

	    surface.blit( self.image, rect )

Now, the image should show instead of the rectangle.


Finer Points
------------

Image Size
-----------

You should make the image the same size as the element
it is representing.  For example, my baddie image should
be 20x20, or I should change the baddie size in 
`GameProgram`'s `__init__` method to match the size
of the image I created.
