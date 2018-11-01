Adding Music to Pygame Programs
-------------------------------

I'm going to add a music soundtrack to my game.

Sound Files
-----------

First, I need to make or find a soundtrack file. There are many
sound file formats.  Pygame supports many of them, but it depends
on your computer system installation.  It's best to get your
music and try it.  If the file doesn't work, convert to another
format and try again.

I've had most success with MP3 and OGG files for soundtracks.
I use the free program Audacity to edit and convert files.

I found my audio soundtrack and named it audio_soundtrack.mp3.


Enabling Sound in Pygame
------------------------

To use sound or music, you need to initialize the sound mixer 
in pygame.  We'll go to SpaceshipData.py, inside the \_\_init\_\_ 
method of SpaceshipData, and add this line, as the first line 
in the method.

    pygame.mixer.init()

You should check your program for syntax errors before proceeding.

(Note: if you have sound and music, this line only needs to occur
once.)

Loading the Music File
----------------------

Next, we'll need to load the music file into the program
so we can play it.  This also needs to be completed in 
ShapeshipData's \_\_init\_\_ method.  Here are the lines I would 
put, right after the line that initializes the sound mixer.

    pygame.mixer.music.load("audio_soundtrack.mp3")

Notice the name of the audio file is in quotes.  This
name must match the file name exactly.  If your operating
system hides the file extension, be sure that you have it
correct.

You should check your program for syntax errors before proceeding.


Playing Music
-------------

Now that the music file is loaded into the program, we need to
make it play.

This also needs to be completed in ShapeshipData's \_\_init\_\_ 
method.  This line should be inserted after the loading of
the music to play the it:

    pygame.mixer.music.play()

You should check your program for syntax errors before 
proceeding.

Run the program.  You should hear the music while the
program is running.

(Note: Only one music file can play at a time, but sounds
can play at the same time as the music file.)


Finer Points
------------

Volume
------

If you need to adjust the relative volume of music vs sounds,
you can do it in the audio editor before you save the files.
Still you may want to do some fine tuning in the software
after loading the music.

This can be done by adding a line to set the volume in
SpaceshipData's \_\_init\_\_ method, right after loading the
music file, and before playing it:

    pygame.mixer.music.set_volume(0.25)

This example plays the soundtrack at 25% volume.

Adjust the music and sound volumes to give the overall feel
you want for your game.

End of Music
------------

You'll want to explore options for restarting the sound
track when it is finished playing.

Sound Track Switching
---------------------

Consider different sound tracks for different parts of
your game.  Or, let the user switch sound tracks.


Aquiring Soundtracks
--------------------

You can search for free music on the internet.  Be careful
not to violate copyrights.  How cool would it be to create
your own soundtrack with GarageBand or some other music
authoring tool?  Can you or your team mates play instruments?

Learning More About Music in Pygame
------------------------------------

* [Music Documentation](http://www.pygame.org/docs/ref/music.html)







