define USAGE
Development:

    simulator     Run application with simulator
    clean
endef
export USAGE

help:
	@echo "$$USAGE"

.NOTPARALLEL:

.rmkit:
	git clone \
	    --depth=1 \
	    https://github.com/rmkit-dev/rmkit.git \
	    .rmkit

.venv/bin/activate:
	@echo "Setting up development virtual env in .venv"
	python -m venv .venv; \
	. .venv/bin/activate; \
	python -m pip install -r requirements-dev.txt

.rmkit/src/build/simple: .rmkit .venv/bin/activate
	. .venv/bin/activate; \
	cd .rmkit; \
	TARGET=dev make simple

define SCRIPT
#!/bin/sh
. .venv/bin/activate
exec python myapp.py --simple-executable=.rmkit/src/build/simple
endef
export SCRIPT

.resim.sh: .rmkit/src/build/simple
	echo "$$SCRIPT" >> .resim.sh
	chmod +x .resim.sh

simulate: .venv/bin/activate .resim.sh
	. .venv/bin/activate; \
	resim ./.resim.sh

clean:
	git clean --force -dX
	rm -rf .rmkit

.PHONY: \
    all \
    simulator \
    clean
