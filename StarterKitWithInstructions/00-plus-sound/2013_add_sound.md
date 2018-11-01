Adding Sound to Pygame Programs
-------------------------------

I'm going to add two sounds to my game.  I'll put a bang when
bullets are fired, and a boom when bullets hit baddies.

Sound Files
-----------

First, I need to make or find the sound files.  There are many
sound file formats.  Pygame supports many of them, but it depends
on your computer system installation.  It's best to get your
sound and try it.  If the sound doesn't work, convert to another
format and try again.

I've had most success with WAV files for sounds.  I use the
free program Audacity to edit and convert sound files.  With
my microphone, I created two sound files: audio_bang.wav and 
audio_boom.wav.


Enabling Sound in Pygame
------------------------

To use sound, you need to initialize the sound mixer in pygame.
We'll go to SpaceshipData.py, inside the \_\_init\_\_ method of
SpaceshipData, and add this line, as the first line in the 
method.

    pygame.mixer.init()

You should check your program for syntax errors before proceeding.

(Note: if you have sound and music, this line only needs to occur
once.)

Loading Sound Files
-------------------

Next, we'll need to load the sound files into the program
so we can play them when the events occur.  This also needs
to be completed in ShapeshipData's \_\_init\_\_ method.  Here
are the lines I would put, right after the line that
initializes the sound mixer.

    self.bang_sound = pygame.mixer.Sound("audio_bang.wav")
    self.boom_sound = pygame.mixer.Sound("audio_boom.wav")

Notice the names of the sound files are in quotes.  These
names must match the file names exactly.  If your operating
system hides the file extension, be sure that you have it
correct.

You should check your program for syntax errors before proceeding.


Playing Sounds
--------------

Now that the sounds are loaded into the program, we need to
make them play whenever the appropriate events occur.

Firing Bullet Sounds
--------------------

Bullets are fired in SpaceshipData's evolve method, near 
the 10th line of the function.  Look for pygame.K_SPACE.  
This looks to see if the user pressed the space bar.

Inside of the if statement (at the same indentation as 
the self.bullets.append), add this line to play the
bang sound.

    self.bang_sound.play()

You should check your program for syntax errors before 
proceeding.

Run the program.  You should hear the bang sound every
time you press the space bar.


Blowing up Baddie Sounds
------------------------

Baddies are destroyed in SpaceshipData's evolve method.
Look for the line that says baddie.setAlive(False).  This
is were they are eliminated.

Right after that line, we'll play the boom sound.  This
needs to be at the same indentation as that line.

    self.boom_sound.play()

You should check your program for syntax errors before 
proceeding.

Run the program.  You should hear the boom sound every
time a baddie is destroyed.


Finer Points
------------

Volume
------

If you need to adjust the relative volumes of the sounds,
you can do it in the audio editor before you save them.
Still you may want to do some fine tuning in the software
after loading the sounds.  

This can be done by adding lines to set the volume in
SpaceshipData's \_\_init\_\_ method, right after loading the
sound files:

    self.bang_sound.set_volume(0.5)
    self.boom_sound.set_volume(0.8)

These examples play the bang sound at 50% and the bang
sound at 80%.

Timing
------

When you create your sounds, make sure there is no silence
at the beginning of the file.  That silence will play before
the audible portion of the file.  That will make the sound
feel delayed.

Aquiring Sounds
---------------

You can search for free sounds on the internet.  However,
it'll be a lot more fun to create your own sounds.  Get
a microphone connected to your system, and play a horn,
tap the table, pop a balloon, etc.  Edit the sound with
Audacity or some other sound editor.

Learning More About Sounds in Pygame
------------------------------------

* [Mixer Documentation](http://www.pygame.org/docs/ref/mixer.html)
* [Sound Documentation](http://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound)







