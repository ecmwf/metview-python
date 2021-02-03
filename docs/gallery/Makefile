.DEFAULT_GOAL := html
.PHONY: all html clean

SRCS := $(wildcard *.py gallery.yaml)

# we do not have the list of all rst targets, so we just pick one both
# from "gallery" and "gallery_backref". These must always be valid rst targets!
GALLERY_TARGET = ../gen_files/gallery/advection.rst
BACKREF_TARGET = ../gen_files/gallery_backref/mcont.rst

$(GALLERY_TARGET): $(SRCS)
	python3 build_gallery.py

$(BACKREF_TARGET): $(SRCS)
	python3 build_gallery.py

html: $(GALLERY_TARGET) $(BACKREF_TARGET)

all: html

clean:
	@echo "cleaning ../gen_files/gallery"
	@rm -rf ../gen_files/gallery/*.rst
	@echo "cleaning ../gen_files/gallery_backref"
	@rm -rf ../gen_files/gallery_backref/*.rst
