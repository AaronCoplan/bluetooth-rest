.PHONY: install run usage

all: usage

usage:
	@echo "Available roles:"
	@echo -e "\tinstall: Installs necessary dependencies."
	@echo -e "\trun: Runs the software.  This may fail if install has not been run."

install:
	./scripts/install-apt.sh

run:
	echo "Running..."
