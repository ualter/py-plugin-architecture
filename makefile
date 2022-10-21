.DEFAULT_GOAL := help
.SHELLFLAGS = -ec

MODULE_NAME:=pycypher

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-18s\033[33m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ --| Utils     |--------------------------------------------------------------------------------------------------------------------------------------

prun:  ## run server using poetry scripts
	clear ; \
	poetry run server ; \
	printf " \n"; \

test: ## run tests
	clear ; \
	poetry run pytest -v -s ; \
	printf " \n"; \

run: ## run FastAPI server for demo
	clear ; \
	uvicorn pycypher.server:app --reload ; \
	printf " \n"; \