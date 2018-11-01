WEBDIR := ../web/spring2012.examples
BASE := RookieKit-2013
PACKAGE_FILES := TODO.txt main.py SpaceshipData.py SpaceshipAdventure.py baddie.py bullet.py game_mouse.py spaceship.py

DEPEND_FILES := Makefile $(PACKAGE_FILES)
ZIP_PACKAGE_FILES := $(foreach f,$(PACKAGE_FILES),$(BASE)/$(f))

all: $(WEBDIR)/$(BASE).zip

$(WEBDIR)/$(BASE).zip: ../$(BASE).zip
	mv ../$(BASE).zip $(WEBDIR)/$(BASE).zip

../$(BASE).zip: $(DEPEND_FILES)
	(cd ..; rm -f $(BASE).zip; zip -r $(BASE).zip $(ZIP_PACKAGE_FILES))

TODO.txt: TODO-linux.txt Makefile
	cat TODO-linux.txt | sed -r 's/$$/\r/' > TODO.txt
