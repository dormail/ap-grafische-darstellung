all: main.pdf

aufgabe1/aufgabe1-plot.pdf: aufgabe1/main.py aufgabe1/daten.csv
	cd aufgabe1 && python3 main.py

aufgabe2/aufgabe2-plot.pdf: aufgabe2/main.py aufgabe2/daten.csv
	cd aufgabe2 && python3 main.py

main.pdf: main.tex aufgabe1/aufgabe1-plot.pdf aufgabe2/aufgabe2-plot.pdf
	lualatex main.tex

clean:
	rm -rf *.pdf *.aux *.dvi *.latexmk *.fls *.log *.out
	cd aufgabe1 && rm -rf *.pdf *.aux *.dvi *.latexmk *.fls *.log *.out
	cd aufgabe2 && rm -rf *.pdf *.aux *.dvi *.latexmk *.fls *.log *.out
	cd aufgabe3 && rm -rf *.pdf *.aux *.dvi *.latexmk *.fls *.log *.out

