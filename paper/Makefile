.PHONY: all clean clean-all pdf

all:
	-xelatex --shell-escape include.tex
	-biber include.bcf
	-xelatex --shell-escape include.tex
	xelatex --shell-escape include.tex

clean:
	rm -f *.aux
	rm -f *.bcf
	rm -f *.log
	rm -f *.out
	rm -f *.run.xml

clean-all: clean pdf

pdf:
	-rm -f include.pdf
