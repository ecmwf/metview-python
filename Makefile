
PACKAGE := mpy
PYTHONS := python3.6 python3.5 pypy3 python3.4

SOURCE := MetviewBundle-2017.12.1-Source.tar.gz
SOURCE_URL := https://software.ecmwf.int/wiki/download/attachments/51731119/$(SOURCE)

DOCKERBUILDFLAGS := --build-arg SOURCE=$(SOURCE)
PIP := pip

export WHEELHOUSE := ~/.wheelhouse
export PIP_FIND_LINKS := $(WHEELHOUSE)
export PIP_WHEEL_DIR := $(WHEELHOUSE)
export PIP_INDEX_URL
TOXFLAGS := --workdir=.docker-tox
MKDIR = mkdir -p

ifeq ($(shell [ -d $(WHEELHOUSE) ] && echo true),true)
    DOCKERFLAGS := -v $(WHEELHOUSE):/root/.wheelhouse -e PIP_INDEX_URL=$$PIP_INDEX_URL
    PIP_FIND_LINKS += $(WHEELHOUSE)
endif

RUNTIME := $(shell [ -f /proc/1/cgroup ] && cat /proc/1/cgroup | grep -q docker && echo docker)
ifneq ($(RUNTIME),docker)
    RUN = docker run --rm -it -v `pwd`:/src $(DOCKERFLAGS) $(PACKAGE)
endif


default:
	@echo No default

# local targets

local-wheelhouse-one:
	$(PIP) install pip setuptools wheel
	$(PIP) wheel -r requirements/requirements-tests.txt
	$(PIP) wheel -r requirements/requirements-docs.txt

local-wheelhouse:
	for PYTHON in $(PYTHONS); do $(MAKE) local-wheelhouse-one PIP="$$PYTHON -m pip"; done
	$(PIP) wheel -r requirements/requirements-dev.txt

local-install-dev-req:
	$(PIP) install -U pip setuptools wheel
	$(PIP) install -r requirements/requirements-dev.txt

local-install-test-req:
	$(PIP) install -r requirements/requirements-tests.txt

local-develop: local-install-dev-req
	$(PIP) install -e .

clean:
	$(RM) -r */__pycache__ */*.pyc htmlcov dist build .coverage .cache .eggs *.egg-info

distclean: clean
	$(RM) -r .tox .docker-tox

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

test:
	$(RUN) pytest -v --flakes --cov=$(PACKAGE) --cov-report=html --cache-clear

qc:
	$(RUN) pytest -v --pep8 --mccabe

tox:
	$(RUN) tox $(TOXFLAGS)

detox:
	$(RUN) detox $(TOXFLAGS)

# image build

$(SOURCE):
	curl -o $(SOURCE) -L $(SOURCE_URL)

image: $(SOURCE)
	docker build -t $(PACKAGE) $(DOCKERBUILDFLAGS) .
