Baddie Collisions with the Spaceship
====================================

I want the a baddie that hits the spaceship to kill 
the spacehip and the baddie.  I also want the game to stop
moving when this occurs.

Luckily, there's already an example with bullets hitting
baddies and killing them.  Let's see if we can do something
similar.

Make the Spaceship Able to be Alive or Dead
-------------------------------------------

Look at `baddie.py`, you'll see that it uses `self.alive`
to keep track of whether the baddie is alive or dead.  There
is nothing in `spaceship.py` to do the same for the spaceship.
Let's add it.

# The spaceship should be alive when it is created.

Add to `Spaceship`'s `__init__` method a property for the spaceship
to make it alive.  Add:

        self.alive  = True
    
When `self.alive` is `True`, the ship is alive.  When it is `False`,
the ship is dead.

# The game program needs to know if the ship is alive or not.

Add to `spaceship.py` a new function:

    def getAlive( self ):
        return self.alive

Be sure that this is not in the middle of lines for another function
that is already there.  Also, make sure it is indented the same as
the other function `def`s in the file.

# The game program needs to tell a ship that is is no longer alive.

Add to `spaceship.py` a new function:

    def setAlive( self, alive ):
        self.alive = alive

Be sure that this is not in the middle of lines for another function
that is already there.  Also, make sure it is indented the same as
the other function `def`s in the file.


Make the Baddies Able to Know If They Hit the Spaceship
-------------------------------------------------------

Look at `bullet.py`.  You'll see `hitRectangle`, and `checkHitBaddie`,
which are used to see if a bullet's rectangle overlaps with
a baddie's rectangle. That's what we mean by "hit".

# The baddie needs to know if it overlaps with a rectangle.

A rectangle is described by x,y which is the location of its
top left corner, and w,h where are the width and height of
the rectangle.

Add to `baddie.py` a new function.  You'll notice this is exactly
like the one in `bullet.py`

    def hitRectangle( self, x, y, w, h ):
        if ( ( ( self.x + self.width ) >= x ) and
             ( self.x <= x + w ) ):
            if ( ( ( self.y + self.height ) >= y ) and
                 ( self.y <= y + h ) ):
                return True
        return False
    
# The baddie needs to know the ship's rectangle information

A ship has a rectangle shape.  It has the four pieces
of information we need to check if the baddie hits its
rectangle.  But, there's not easy way to give it to
the baddie.

Look at `baddie.py`, there is a function `getDimensions`
that returns a baddie's rectangle information.  Add the same
function to `spaceship.py`:

    def getDimensions( self ):
        return self.x, self.y, self.width, self.height

# The baddie needs to know if it hits the ship

Now, we're ready for the baddie to check if it hits the
spaceship. Add a new function to `baddie.py` that gets the 
ship's rectangle information and uses that to call `hitRectangle`:

    def hitsShip( self, ship ):
        x, y, w, h = ship.getDimensions( )
        if self.hitRectangle( x, y, w, h ):
            return True
        else:
            return False

Notice this function returns `True` if the ship is hit,
and `False` if the ship is not hit.

# The game program needs to check if any baddie hits the spaceship

The game program already checks if any bullet hits any baddie.  We
will now have it check if any baddie hits the spaceship.  Find
the `evolve` function in `game_program.py`.  Find the place where
bullets hitting baddies is checked.  After that, but before the
place where deactivated bullets and baddies are removed, add
this code.

        # check if any baddie kills the spaceship
        for baddie in self.baddies:
            if not baddie.getAlive( ):
                continue
            if baddie.hitsShip( self.spaceship ):
                self.spaceship.setAlive( False )
                baddie.setAlive( False )

Note this kills the baddie and the spaceship on collision.


# The game program needs to stop moving if the ship is dead

Go to the begging of the `evolve` function of `spaceship.py`,
and add this:

        # stop if spaceship is dead
        if not self.spaceship.getAlive( ):
            return

This will cause the `evolve` function to do nothing (that is
not move anything) if the ship is dead.

Try It Out
-----------

Did you save the files that were changed?  If not, do it now.
Run the program, and steer the spaceship into a baddie.  Does
the baddie disappear, and everything else freezes?  If so, 
you did it!  If not, go back through all of the details and
see if you can find something that is not correct.
