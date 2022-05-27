# detect OS ------------------------------------------------------
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
	os_string := win
	os_shell := powershell
	rm_lib_sh := .\poetry_remove_lib.ps1 -MssName
	pushd_cmd := powershell Push-Location
	popd_cmd := powershell Pop-Location
else
    detected_OS := $(shell uname)
	os_string := nix
	os_shell := bash
	rm_lib_sh := poetry_remove_lib.sh
	pushd_cmd := pushd
	popd_cmd := popd
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

clean:
	$(os_shell) $(rm_lib_sh) "askowl"

all:
	make clean
	make build
	poetry run python -m pip install --upgrade pip
# -----------------------------------------------------------------

# DEBUG Commands --------------------------------------------------
info:
	echo $(detected_OS)
	echo $(os_string)
	echo $(SHELL)
# -----------------------------------------------------------------
