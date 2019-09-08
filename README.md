# CIRI-long
Circular RNA Identification for Nanopore Sequencing 

#### Dependency

- **Only python3 is supported**
- CIRI-long requires pysam lib, which need executable and header of zlib, bzip2, xz, 
please refer to documentation of pysam for detailed information
- all python dependencies are listed in `requirements.txt`


#### Installation

You can simply clone the whole repository, then use `make` to start a complete installation 

```bash
git clone https://github.com/Kevinzjy/CIRI-long.git CIRI-long
cd CIRI-long

# Install submodule
git submodule init 
git submodule update

# Install CIRI-long 
make
```

**Note**: for expert users, the installation under virtualenv is highly recommended

```bash
git clone https://github.com/Kevinzjy/CIRI-long.git CIRI-long
cd CIRI-long

# Install submodule
git submodule init 
git submodule update

# Create virtual environment
python3 -m venv venv

# Activate virtualenv
source ./venv/bin/activate

# Install CIRI-long
make

# Deactivate
deactivate
```