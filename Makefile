CXX=g++
CXXFLAGS=-std=c++20 -Wall -lgsl

.PHONY: graph
.PRECIOUS: %.x

all: coupled

coupled: coupled.x code/work.py
	./coupled.x 51 0.01 2000
	python code/work.py

rand_lf.x: code/rand_lf.cpp code/rand_lf.hpp
	$(CXX) $(CXXFLAGS) $< -o $@

coupled.x: code/coupled.cpp code/coupled.hpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	@find . -type f -name "*.dat" -delete
	@find . -type f -name "*.x" -delete
clean_results:
	@find . -type f -name "*.pdf" -delete
	@find . -type f -name "*.png" -delete
