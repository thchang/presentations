FNAME = thchang-slides
CHART = algorithm-chart

all : $(FNAME).pdf
	open $(FNAME).pdf

$(FNAME).pdf : $(FNAME).tex $(CHART).pdf
	pdflatex $(FNAME).tex
	pdflatex $(FNAME).tex
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out

$(CHART).pdf : $(CHART).tex
	pdflatex $(CHART).tex
	rm -f $(CHART).log $(CHART).aux

clean :
	rm -f $(FNAME).log $(FNAME).aux $(FNAME).nav \
		$(FNAME).toc $(FNAME).snm $(FNAME).out \
		$(FNAME).pdf $(CHART).pdf *-eps-converted-to.pdf
