.DEFAULT_GOAL := html
.PHONY: all html metview clean

SRCS := $(wildcard *.py ../examples/*.ipynb)

# we do not have the list of all rst targets, so we just pick one 
# from "nb_backref". This must always be exist!
BACKREF_TARGET = ../gen_files/nb_backref/mcont.rst

$(BACKREF_TARGET): $(SRCS)
	python3 build_nb.py

metview: $(BACKREF_TARGET)
html: metview
all: metview

clean:
	@echo "cleaning ../gen_files/nb_backref"
	@rm -rf ../gen_files/nb_backref/*.rst
