# Makefile for 


HEADER = parmoo_mdml_cfr_poster
PICS = ../img
#BIB = .
TEX = . 
PY = .

TARGETS: $(HEADER).pdf

tex_files = $(shell find $(TEX) -name '*.tex' -print)
bib_files = $(shell find $(BIB) -name '*.bib' -print)
py_files = $(shell find $(PY) -name '*.py' -print)
pic_files = $(shell find $(PICS) \
		\( -name '*.eps' -print \) -or \( -name '*.epsi' -print \) \
		-or \( -name '*.ps' -print \) -or \( -name '*.png' -print \) \
		-or \( -name '*.fig' -print \) -or \( -name '*.pdf' -print \) \
                -or \( -name '*.tikz' -print \) \
	)

%.pdf: %.tex $(tex_files) $(bib_files) $(pic_files) $(py_files)
	pdflatex $(HEADER)
	#bibtex $(HEADER)
	#pdflatex $(HEADER)
	pdflatex $(HEADER)
	#biber $(HEADER)
	#pdflatex -shell-escape $(HEADER)	
	#pdflatex -shell-escape $(HEADER)	
	#dvipdf $(HEADER)

clean:
	find . \( -name '*.blg' -print \) -or \( -name '*.aux' -print \) -or \
		\( -name '*.bbl' -print \) -or \( -name '*~' -print \) -or \
		\( -name '*.spl' -print \) -or \
		\( -name '*.run.xml' -print \) -or \
		\( -name '*.bcf' -print \) -or \
		\( -name '*.lof' -print \) -or \( -name '*.lot' -print \) -or \
		\( -name '*.log' -print \) -or \( -name '*.brf' -print \) -or \
		\( -name '*.toc' -print \) -or \( -name '*.toc.old' -print \) | xargs rm -f; \
	rm -f $(HEADER).dvi $(HEADER).log $(HEADER).ps $(HEADER).pdf $(HEADER).out \
		_region_* TAGS 
