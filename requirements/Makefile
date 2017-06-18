# Based  on
# http://jamescooke.info/a-successful-pip-tools-workflow-for-managing-python-package-requirements.html


ins = $(wildcard *.in)
outputs := $(ins:.in=.txt)

.PHONY: all
all: $(outputs)


.PHONY: check_pip_tools
check_pip_tools:
	@which pip-compile > /dev/null
	@which pip-sync > /dev/null


%.txt: %.in
	pip-compile --output-file $@ $<

development.txt: check_pip_tools common.txt


.PHONY: clean
clean: check_pip_tools
	rm *.txt


.PHONY: sync_development
sync_development:
	pip-sync development.txt
