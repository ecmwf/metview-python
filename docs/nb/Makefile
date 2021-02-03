.PHONY: all html clean

SRCS := $(wildcard *.py ../examples/*.ipynb)

# we do not have the list of all rst targets, so we just pick one 
# from "bn_backre". These must always be exist!
BACKREF_TARGET = ../gen_files/gallery_backref/mcont.rst

$(BACKREF_TARGET): $(SRCS)
	python3 build_nb.py

html: $(BACKREF_TARGET)

all: html

clean:
	@echo "cleaning ../gen_files/nb_backref"
	@rm -rf ../gen_files/nb_backref/*.rst
