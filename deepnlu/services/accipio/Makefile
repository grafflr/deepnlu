# detect OS ------------------------------------------------------
ifeq ($(OS),Windows_NT)
    detected_OS := Windows
	os_string := win
	os_shell := powershell
	rm_lib_sh := ../../../resources/scripts/Poetry-Remove-Lib.ps1 -MssName
	pushd_cmd := powershell Push-Location
	popd_cmd := powershell Pop-Location
	regression_run_sh := powershell .\scripts\Run-Regression.ps1 -FilePath
else
    detected_OS := $(shell uname)
	os_string := nix
	os_shell := $(SHELL)
	rm_lib_sh := ../../../resources/scripts/poetry_remove_lib.sh
	pushd_cmd := pushd
	popd_cmd := popd
	regression_run_sh := ./scripts/run_regression.sh
endif
# ----------------------------------------------------------------

# Environment Variables-------------------------------------------
# -----------------------------------------------------------------

# Build Commands -------------------------------------------------
install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings -v

clean:
	$(os_shell) $(rm_lib_sh)  "datablock"

build:
	make install
	make test
	poetry build

regressl:
	$(pushd_cmd) ../../utils/regressl ; $(regression_run_sh) "../../services/accipio/regression" ; $(popd_cmd)

all:
	make clean
	make build
	make regressl
	poetry run python -m pip install --upgrade pip
# -----------------------------------------------------------------

# DEBUG Commands --------------------------------------------------
info:
	echo $(detected_OS)
	echo $(os_string)
	echo $(SHELL)
	echo $(rm_lib_sh)
	echo $(regression_run_sh)
	echo $(pushd_cmd)
	echo $(popd_cmd)
# -----------------------------------------------------------------
