
PACKAGE := metview
IMAGE := $(PACKAGE)
MODULE := $(PACKAGE)
PYTHONS := python3.6 python3.5 python3.4 pypy3

SOURCE := MetviewBundle-2019.02.0-Source.tar.gz
SOURCE_URL := https://software.ecmwf.int/wiki/download/attachments/51731119/$(SOURCE)

# uncomment after running the command 'make local-wheel' in the xarray-grib folder
# EXTRA_PACKAGES := xarray_grib-0.1.0-py2.py3-none-any.whl

export WHEELHOUSE := ~/.wheelhouse
export PIP_FIND_LINKS := $(WHEELHOUSE)
export PIP_WHEEL_DIR := $(WHEELHOUSE)
export PIP_INDEX_URL

DOCKERBUILDFLAGS := --build-arg SOURCE=$(SOURCE)
DOCKERFLAGS := -e WHEELHOUSE=$(WHEELHOUSE) \
	-e PIP_FIND_LINKS=$(PIP_FIND_LINKS) \
	-e PIP_WHEEL_DIR=$(PIP_WHEEL_DIR) \
	-e PIP_INDEX_URL=$$PIP_INDEX_URL
# Development options
# DOCKERFLAGS += -v $$(pwd)/../metview:/tmp/source/metview
# DOCKERFLAGS += -v $$(pwd)/../metview-prefix:/usr/local
# DOCKERFLAGS += -v $$(pwd)/../metpy:/metpy
PIP := pip
MKDIR = mkdir -p

ifeq ($(shell [ -d $(WHEELHOUSE) ] && echo true),true)
    DOCKERFLAGS += -v $(WHEELHOUSE):/root/.wheelhouse
endif

RUNTIME := $(shell [ -f /proc/1/cgroup ] && cat /proc/1/cgroup | grep -q docker && echo docker)
ifneq ($(RUNTIME),docker)
    override TOXFLAGS += --workdir=.docker-tox
    RUN = docker run --rm -it -v$$(pwd):/src -w/src $(DOCKERFLAGS) $(IMAGE)
endif


default:
	@echo No default

# local targets

$(PIP_FIND_LINKS):
	$(MKDIR) $@

local-wheelhouse-one:
	$(PIP) install wheel
	$(PIP) wheel -r requirements/requirements-tests.txt
	$(PIP) wheel -r requirements/requirements-docs.txt

local-wheelhouse:
	for PYTHON in $(PYTHONS); do $(MAKE) local-wheelhouse-one PIP="$$PYTHON -m pip"; done
	$(PIP) wheel -r requirements/requirements-dev.txt

local-install-dev-req:
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements/requirements-dev.txt

local-install-test-req: $(PIP_FIND_LINKS)
	$(PIP) install -r requirements/requirements-tests.txt

local-develop: $(EXTRA_PACKAGES)
	for p in $<; do $(PIP) install $$p; done
	$(PIP) install -e .

local-wheel:
	$(PIP) wheel -e .

testclean:
	$(RM) -r */__pycache__ .coverage .cache

clean:
	$(RM) -r */*.pyc htmlcov dist build .eggs *.egg-info

distclean: clean
	$(RM) -r .tox .docker-tox

cacheclean:
	$(RM) -r $(WHEELHOUSE)/* ~/.cache/*

# container targets

shell:
	$(RUN)

notebook: DOCKERFLAGS += -p 8888:8888
notebook:
	$(RUN) jupyter notebook --ip=* --allow-root

wheelhouse:
	$(RUN) make local-wheelhouse

update-req:
	$(RUN) pip-compile -o requirements/requirements-tests.txt -U setup.py requirements/requirements-tests.in
	$(RUN) pip-compile -o requirements/requirements-docs.txt -U setup.py requirements/requirements-docs.in

test: testclean
	$(RUN) python setup.py test --addopts "-v --flakes --cov=$(MODULE) --cov-report=html --cache-clear"

qc:
	$(RUN) python setup.py test --addopts "-v --pep8 --mccabe metview tests"

tox: testclean
	$(RUN) tox $(TOXFLAGS)

detox: testclean
	$(RUN) detox $(TOXFLAGS)

# image build

%.whl: $(WHEELHOUSE)/%.whl
	cp -a $< $@

$(SOURCE):
	curl -o $@ -L $(SOURCE_URL)

image: $(SOURCE) $(EXTRA_PACKAGES)
	docker build -t $(IMAGE) $(DOCKERBUILDFLAGS) .
