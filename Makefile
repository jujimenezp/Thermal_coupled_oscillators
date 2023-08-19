CXX=g++
CXXFLAGS=-std=c++20 -Wall -lgsl

.PHONY: graph
.PRECIOUS: %.x

all: rand_lf.x

rand_lf.x: code/rand_lf.cpp code/rand_lf.hpp
	$(CXX) $(CXXFLAGS) $< -o $@

graph: rand_lf.x results/hay.dat results/no_hay.dat
	code/graph.py

clean:
	@find . -type f -name "*.dat" -delete
	@find . -type f -name "*.x" -delete
clean_results:
	@find . -type f -name "*.pdf" -delete
	@find . -type f -name "*.png" -delete
