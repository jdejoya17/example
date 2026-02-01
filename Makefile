SHELL := /bin/bash

ifneq (,$(wildcard ./.env))
 include ./.env
 export
endif

#####################################################
# Install Targets
#####################################################
##@ Installers
.PHONY: install-openapi-merge
install-openapi-merge: ## installs openapi merger tool
	@command -v npm >/dev/null 2>&1 || { \
		printf "${RED}ERROR${NC}: npm is not installed\n"; \
		printf "Please install Node.js (which includes npm): https://nodejs.org/\n"; \
		exit 1; \
	}
	@npm install -g openapi-merge-cli


#####################################################
# Utility Targets
#####################################################
##@ Utilities 
.PHONY: help
help: ## display help information
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make ${LIGHT_BLUE}<target>${NC}\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  ${LIGHT_BLUE}%-40s${NC} %s\n", $$1, $$2 } /^##@/ { printf "\n${BOLD}%s${NC}\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: merge-openapi-specs
merge-openapi-specs: ## merges the openapi specification files
	@command -v openapi-merge-cli >/dev/null 2>&1 || { \
		printf "${RED}ERROR${NC}: openapi-merge-cli not installed\n"; \
		exit 1; \
	}; \
	@set -euo pipefail; \
	rm -f ${OPENAPI_SPEC_BASE_DIR}/${MERGED_SPEC_FILENAME}; \
	mapfile -t YAML_FILES < <( \
		find "${OPENAPI_SPEC_BASE_DIR}" \
			-type d -name templates -prune -o \
	    	-type f \( -name '*.yaml' -o -name '*.yml' \) -print | LC_ALL=C sort \
	); \
	{ \
		echo "inputs:"; \
	  	for file in "$${YAML_FILES[@]}"; do \
			rel_path=$$(realpath --relative-to="${CONFIGS_BASE_DIR}" "$$file"); \
	   		echo "  - inputFile: $$rel_path"; \
	 	done; \
	  	echo "output: ../${OPENAPI_SPEC_BASE_DIR}/${MERGED_SPEC_FILENAME}"; \
	} > "${OPENAPI_SPEC_MERGE_CONFIG}"; \
	openapi-merge-cli -c $(OPENAPI_SPEC_MERGE_CONFIG)
	