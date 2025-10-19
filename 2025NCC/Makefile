FNAME = main

all : $(FNAME).pdf

$(FNAME).pdf : $(FNAME).tex
	pdflatex $(FNAME).tex
	pdflatex $(FNAME).tex
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out header.aux

clean :
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out header.aux \
		$(FNAME).pdf $(CHART).pdf *-eps-converted-to.pdf
