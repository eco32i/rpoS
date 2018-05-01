# rpoS
Scripts for rpoS paper

# Setup

Clone the repo:

`$ git clone https://github.com/eco32i/rpoS.git`

If you want to use `python 3` virtualenv (tested on Ubuntu 16.04):

- Navigate to `rpoS/scripts` and run the `bootstrap.sh` script that will install system wide dependencies and create Python 3 virtual environment called `rpoS` in `$HOME/.venv`:

   `$ ./bootstrap.sh --all`

   The list of installed packages in the final virtualenv is given in `requirements.txt` file. However, installing with `pip -r requirements.txt` is not recommended as the order of installation is important. 

If you want to use `conda` environment (should work on Mac, Windows and Linux platforms):

- Install [`miniconda`](http://conda.pydata.org/miniconda.html)
- From `rpoS` directory run:

   `$ conda env create -f environment.yml`

To run the notebooks, activate `rpoS` environment:

`$ source ~/.venv/rpoS/bin/activate`

Or, if you are using `conda` environment:

`$ source activate rpoS`

Then go to `notebooks` directory and start `jupyter` session:

`$ jupyter notebook`

# Data download

You can download the data by running `notebooks/Data download.ipynb` notebook.
