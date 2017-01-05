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
Alternatively you can use your FTP client of choice to download data files from the FTP server using the following configuration:

>server: `ftp://ftp.ivsphoto.net`

>username: `rpoS@ivsphoto.net`

>password: `o+"&cLF5O({B`

After downloading the files put them in the `data` directory.

```
18826_ATCACG_H8FKYADXX_1_20140410B_20140410.bam - WT stationary rep 1
18828_TTAGGC_H8FKYADXX_1_20140410B_20140410.bam - sRNA triple mutant stationary rep 1
18832_ACAGTG_H8FKYADXX_2_20140410B_20140410.bam - WT stationary rep 2
18834_GATCAG_H8FKYADXX_2_20140410B_20140410.bam - sRNA triple mutant stationary rep 2
19255_ATCACG_H8UHCADXX_1_20140509B_20140509.bam - WT exponential rep 1
19256_CGATGT_H8UHCADXX_1_20140509B_20140509.bam - WT+BCM exponential rep 1
19257_TTAGGC_H8UHCADXX_1_20140509B_20140509.bam - sRNA triple mutant exponential rep 1
19261_ACAGTG_H8UHCADXX_2_20140509B_20140509.bam - WT exponential rep 2
19262_GCCAAT_H8UHCADXX_2_20140509B_20140509.bam - WT+BCM exponential rep 2
19263_GATCAG_H8UHCADXX_2_20140509B_20140509.bam - sRNA triple mutant exponential rep 2
```
