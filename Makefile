# detect OS ------------------------------------------------------
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
	os_string := win
else
    detected_OS := $(shell uname)
	os_string := nix
endif
# ----------------------------------------------------------------

# Build Commands -------------------------------------------------
install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build

all:
	make build
	poetry run python -m pip install --upgrade pip
# -----------------------------------------------------------------

# DEBUG Commands --------------------------------------------------
info:
	echo $(detected_OS)
	echo $(os_string)
	echo $(SHELL)
# -----------------------------------------------------------------
