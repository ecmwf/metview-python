
PACKAGE := metview
IMAGE := $(PACKAGE)-ci
MODULE := $(PACKAGE)
PYTHONS := python3.6 python3.5 python3.4 pypy3
PYTHON := python

SOURCE_NAME := MetviewBundle-2018.10.0-Source.tar.gz
SOURCE := ci/$(SOURCE_NAME)
SOURCE_URL := https://software.ecmwf.int/wiki/download/attachments/51731119/$(SOURCE_NAME)

PYTESTFLAGS_TEST := -v --flakes --doctest-glob '*.rst' --cov=$(MODULE) --cov-report=html --cache-clear
PYTESTFLAGS_QC := --pep8 --mccabe $(PYTESTFLAGS_TEST)

export WHEELHOUSE := ~/.wheelhouse
export PIP_FIND_LINKS := $(WHEELHOUSE)
export PIP_WHEEL_DIR := $(WHEELHOUSE)
export PIP_INDEX_URL

DOCKERBUILDFLAGS := --build-arg SOURCE=$(SOURCE)
DOCKERFLAGS := -e WHEELHOUSE=$(WHEELHOUSE) \
	-e PIP_FIND_LINKS=$(PIP_FIND_LINKS) \
	-e PIP_WHEEL_DIR=$(PIP_WHEEL_DIR) \
	-e PIP_INDEX_URL=$$PIP_INDEX_URL
PIP := $(PYTHON) -m pip
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
	$(PIP) wheel -r ci/requirements-tests.txt
	$(PIP) wheel -r ci/requirements-docs.txt

local-wheelhouse:
	for PYTHON in $(PYTHONS); do $(MAKE) local-wheelhouse-one PYTHON=$$PYTHON; done
	$(PIP) wheel -r ci/requirements-dev.txt

local-install-dev-req:
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r ci/requirements-dev.txt

local-install-test-req: $(PIP_FIND_LINKS)
	$(PIP) install -r ci/requirements-tests.txt

local-develop:
	$(PIP) install -e .

local-wheel:
	$(PIP) wheel -e .

testclean:
	$(RM) -r */__pycache__ .coverage .cache

clean: testclean
	$(RM) -r */*.pyc htmlcov dist build .eggs

distclean: clean
	$(RM) -r .tox .docker-tox *.egg-info

cacheclean:
	$(RM) -r $(WHEELHOUSE)/* ~/.cache/*

# container targets

shell:
	$(RUN)

notebook: DOCKERFLAGS += -p 8888:8888
notebook:
	$(RUN) jupyter notebook --ip=0.0.0.0 --allow-root

wheelhouse:
	$(RUN) make local-wheelhouse

update-req:
	$(RUN) pip-compile -o ci/requirements-tests.txt -U setup.py ci/requirements-tests.in
	$(RUN) pip-compile -o ci/requirements-docs.txt -U setup.py ci/requirements-docs.in

test: testclean
	$(RUN) $(PYTHON) setup.py test --addopts "$(PYTESTFLAGS_TEST)"

qc: testclean
	$(RUN) $(PYTHON) setup.py test --addopts "$(PYTESTFLAGS_QC)"

doc:
	$(RUN) $(PYTHON) setup.py build_sphinx

tox: testclean
	$(RUN) tox $(TOXFLAGS)

detox: testclean
	$(RUN) detox $(TOXFLAGS)

# image build
$(SOURCE):
	curl -o $@ -L $(SOURCE_URL)

image: $(SOURCE)
	docker build -t $(IMAGE) -f ci/Dockerfile $(DOCKERBUILDFLAGS) .
