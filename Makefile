# detect OS ------------------------------------------------------
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
	os_string := win
	os_shell := powershell
	rm_lib_sh := .\scripts\poetry_remove_lib.ps1 -MssName
	pushd_cmd := powershell Push-Location
	popd_cmd := powershell Pop-Location
	copy_lib := .\scripts\copy.ps1
else
    detected_OS := $(shell uname)
	os_string := nix
	os_shell := bash
	rm_lib_sh := scripts/poetry_remove_lib.sh
	pushd_cmd := pushd
	popd_cmd := popd
	copy_lib := scripts/copy.sh
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

copy:
	$(os_shell) $(copy_lib)

all:
	make clean
	make build
	poetry run python -m pip install --upgrade pip
# -----------------------------------------------------------------

askowl:
	$(os_shell) $(rm_lib_sh) "askowl"
	poetry install
	poetry build

