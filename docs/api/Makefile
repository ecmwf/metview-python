
.DEFAULT_GOAL := html
.PHONY: all html metview clean

ICON_SRCS := $(wildcard build_icon.py functions.yaml icon_desc/*.yaml icon_desc/*.rst icon_desc/include/*.yaml)
TOC_SRCS = build_toc.py functions.yaml toc.yaml 

# we do not have the list of all rst targets, so we just pick one both
# from "icon_functions" and "toc". These must always be valid rst targets!
ICON_TARGET = ../gen_files/icon_functions/mcont.rst
TOC_TARGET = ../gen_files/toc/grib.rst

$(ICON_TARGET): $(ICON_SRCS)
	python3 build_icon.py

$(TOC_TARGET): $(TOC_SRCS)
	python3 build_toc.py

metview: $(ICON_TARGET) $(TOC_TARGET)
html: metview
all: metview

clean:
	@echo "cleaning ../gen_files/icon_functions"
	@rm -rf ../gen_files/icon_functions/*.rst
	@echo "cleaning ../gen_files/toc"
	@rm -rf ../gen_files/toc/*.rst

