New Game
====================================

I already completed the [Spaceship Dies tutorial](add_baddie_spaceship_collision.md).
Now, I want to be able to start a new game when the spaceship
is hit by a baddie.

I choose to make it so that the user can press the `r` key
to start a new game, but only when the spaceship is dead.

# Make a `newGame` function

In `game_program.py` I'll add this function that makes the
spaceship be alive again, and all all bullets and baddies
from the game.  That will make the game back to the starting
conditions.

    def newGame( self ):
        self.spaceship.setAlive( True )
        self.bullets = [ ]
        self.baddies = [ ]
        return

# Accept `r` key if the spaceship is dead

In the `evolve` function of `game_program.py`, we already have a line
to check if the spaceship is dead and not move the game any more.

        if not self.spaceship.getAlive( ):
            return

We'll add to it so that the user can press `r` if the space is not
dead, and if they do, we'll call `newGame`.

        if not self.spaceship.getAlive( ):
            if pygame.K_r in newkeys:
                self.newGame( )
            return

Try It Out
-----------

Did you save the files that were changed?  If not, do it now.
Run the program, and steer the spaceship into a baddie.  The 
baddie disappears, and everything else freezes?  Now, press
`r`.  Does the game restart?  If so, you did it!  If not, go 
back through all of the details and see if you can find something
that is not correct.
