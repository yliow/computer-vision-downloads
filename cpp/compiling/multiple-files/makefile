#------------------------------------------------------------------------------
# Computer vision
# Makefile for *.cpp
# Y. Liow
#------------------------------------------------------------------------------
# Macros
#------------------------------------------------------------------------------
CXX       = g++
CXXFLAGS  = -g -Wall -fmax-errors=3 -std=c++17 `pkg-config --cflags --libs opencv`
LINK      = g++
LINKFLAGS = `pkg-config --cflags --libs opencv`
OBJS      = main.o
EXE       = main.exe

#------------------------------------------------------------------------------
# Executable
#------------------------------------------------------------------------------
$(EXE):	*.cpp *.h
	$(CXX) *.cpp -o $(EXE) $(CXXFLAGS) -g -fsanitize=address

clean:
	rm -rf $(EXE)
c:
	rm -rf $(EXE)

run:
	./$(EXE)
r:
	./$(EXE)
