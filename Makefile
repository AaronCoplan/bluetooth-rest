.PHONY: install run usage

all: usage

usage:
	@echo "Available roles:"
	@echo -e "\tinstall: Installs necessary dependencies."

install:
	./scripts/install-apt.sh

