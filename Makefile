.PHONY: all lib CIRI_long test

all: lib CIRI-long

CIRI-long:
	cat requirements.txt | xargs -n 1 pip3 install
	python3 setup.py install

lib:
	mkdir -p spoa/build
	cd spoa/build && cmake -DCMAKE_BUILD_TYPE=Release .. && make

test:
	python3 setup.py build_ext --inplace
	mv poa.cpython-36m-x86_64-linux-gnu.so ./CIRI
