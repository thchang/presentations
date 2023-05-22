FNAME = thchang-slides

all : $(FNAME).pdf
	open $(FNAME).pdf

$(FNAME).pdf : $(FNAME).tex
	pdflatex $(FNAME).tex
	pdflatex $(FNAME).tex
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out

clean :
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out \
		$(FNAME).pdf
