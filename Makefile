PYTHON_I_MD = i/??-*.md
PYTHON_II_MD = ii/??-*.md
PANDOC = pandoc -s --toc --number-sections -V colorlinks

all: python-i.pdf python-ii.pdf

python-i.pdf: Makefile $(PYTHON_I_MD)
	$(PANDOC) $(PYTHON_I_MD) -o $@
python-ii.pdf: Makefile $(PYTHON_II_MD)
	$(PANDOC) $(PYTHON_II_MD) -o $@
