
METVIEW_BUNDLE := MetviewBundle-2017.12.1-Source.tar.gz
METVIEW_BUNDLE_URL := https://software.ecmwf.int/wiki/download/attachments/51731119/$(METVIEW_BUNDLE)

PACKAGE := mpy
PIP := pip
PYTHONS := python3.4 python3.5 python3.6 pypy3

export PIP_FIND_LINKS := requirements/wheelhouse
TOXFLAGS := --workdir=.docker-tox
MKDIR = mkdir -p

RUNTIME := $(shell [ -f /proc/1/cgroup ] && cat /proc/1/cgroup | grep -q docker && echo docker)
ifneq ($(RUNTIME),docker)
    RUN := docker run --rm -it -v `pwd`:/src $(PACKAGE)
endif


default:
	@echo No default

# local targets

$(PIP_FIND_LINKS):
	$(MKDIR) $(PIP_FIND_LINKS)

local-wheelhouse-one: $(PIP_FIND_LINKS)
	$(PIP) install pip setuptools wheel
	$(PIP) wheel -w $(PIP_FIND_LINKS) -r requirements/requirements-tests.txt
	$(PIP) wheel -w $(PIP_FIND_LINKS) -r requirements/requirements-dev.txt

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
	$(RM) -r .tox .docker-tox */__pycache__ */*.pyc htmlcov dist build .coverage .cache .eggs *.egg-info

distclean: clean
	$(RM) -r requrements/wheelhouse

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

$(METVIEW_BUNDLE):
	curl -o $(METVIEW_BUNDLE) -L $(METVIEW_BUNDLE_URL)

image: $(METVIEW_BUNDLE)
	docker build -t $(PACKAGE) --build-arg METVIEW_BUNDLE=$(METVIEW_BUNDLE) .
