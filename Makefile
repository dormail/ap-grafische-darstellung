all: main.pdf

aufgabe1/aufgabe1-plot.pdf: aufgabe1/main.py aufgabe1/daten.csv
	cd aufgabe1 && python3 main.py

main.pdf: main.tex aufgabe1/aufgabe1-plot.pdf
	lualatex main.tex
