
PACKAGE := mpy
PYTHONS := python3.4 python3.5 python3.6 pypy3

SOURECE := MetviewBundle-2017.12.1-Source.tar.gz
SOURCE_URL := https://software.ecmwf.int/wiki/download/attachments/51731119/$(SOURCE)

DOCKERBUILDFLAGS := --build-arg SOURCE=$(SOURCE)
PIP := pip
PACKAGEWHEELHOUSE := requirements/wheelhouse

export PIP_FIND_LINKS := $(PACKAGEWHEELHOUSE)
TOXFLAGS := --workdir=.docker-tox
MKDIR = mkdir -p

USERWHEELHOUSE := ~/.wheelhouse
ifeq ($(shell [ -d $(USERWHEELHOUSE) ] && echo true),true)
    DOCKERFLAGS := -v $(USERWHEELHOUSE):/src/$(PACKAGEWHEELHOUSE)
    PIP_FIND_LINKS += $(USERWHEELHOUSE)
endif

RUNTIME := $(shell [ -f /proc/1/cgroup ] && cat /proc/1/cgroup | grep -q docker && echo docker)
ifneq ($(RUNTIME),docker)
    RUN := docker run --rm -it -v `pwd`:/src $(DOCKERFLAGS) $(PACKAGE)
endif


default:
	@echo No default

# local targets

local-wheelhouse-one:
	$(PIP) install pip setuptools wheel
	$(PIP) wheel -w $(PACKAGEWHEELHOUSE) -r requirements/requirements-tests.txt
	$(PIP) wheel -w $(PACKAGEWHEELHOUSE) -r requirements/requirements-dev.txt

local-wheelhouse:
	for PYTHON in $(PYTHONS); do $(MAKE) local-wheelhouse-one PIP="$$PYTHON -m pip"; done

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
	$(RM) -r .tox .docker-tox requirements/wheelhouse

# container targets

shell:
	$(RUN)

wheelhouse:
	$(RUN) make local-wheelhouse

update-test-req:
	$(RUN) pip-compile -o requirements/requirements-tests.txt -U setup.py requirements/requirements-tests.in

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
	-[ -d $(USERWHEELHOUSE) ] && rsync -av --include="*cp36*manylinux*" --exclude="*" $(USERWHEELHOUSE)/ $(PACKAGEWHEELHOUSE)/
	docker build -t $(PACKAGE) $(DOCKERBUILDFLAGS) .
