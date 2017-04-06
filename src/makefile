PYTHON = python
PYFLAGS = -m py_compile
ZIP = zip

ifndef ComSpec
#Unix-definitions
	PATHSEP=/
	CMDSEP=;
	RM=rm -f
	CP=cp
	MD=mkdir
else
#Windows-definitions
	PATHSEP=\\
	CMDSEP=&
	RM=del /F /Q
	CP=copy
	MD=mkdir
endif

_TARGET = ../build/liMO.zip
LIBS_DIR = libs
PLUGINS_DIR = plugins
SRC := $(subst /,$(PATHSEP),$(wildcard *.py) $(wildcard $(LIBS_DIR)/*.py) $(wildcard $(PLUGINS_DIR)/*.py))
COMPILED := $(subst .py,.pyc,$(SRC))
TARGET := $(subst /,$(PATHSEP),$(_TARGET))
COMPRESS := $(subst /,$(PATHSEP),$(wildcard *.py) $(wildcard $(LIBS_DIR)/*.py))

all: $(TARGET)

$(TARGET): $(COMPILED)
	$(ZIP) -r $(TARGET) $(COMPRESS)

%.pyc: %.py
	$(PYTHON) $(PYFLAGS) $^

clean:
	$(RM) $(COMPILED) $(CMDSEP) \
	$(RM) $(subst /,$(PATHSEP),../build/*)
