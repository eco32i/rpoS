#!/bin/bash -e 
tabs 4
clear
readonly VENV_DIR=$HOME/.venv
readonly ENV="rpoS"

install_deps() {
    sudo apt update
    sudo apt install -y 
        libcurl4-openssl-dev python-dev python3-dev build-essential git \
        libhdf5-10 hdf5-tools libopenblas-base libopenblas-dev gfortran \
        g++ python-pip samtools bedtools libpng-dev libjpeg8-dev \
        libfreetype6-dev libxft-dev libhdf5-dev libatlas3-base libatlas-dev \
        python3-venv libxml2-dev libxslt-dev
    sudo update-alternatives --set libblas.so.3 /usr/lib/openblas-base/libblas.so.3
    sudo update-alternatives --set liblapack.so.3 /usr/lib/openblas-base/liblapack.so.3
}


setup_env() {
    local pydata="requirements.txt"
    
    if [ -d $VENV_DIR/rpoS ]
    then
        rm -rf $VENV_DIR/rpoS
    fi

    pyvenv $VENV_DIR/rpoS
    source $VENV_DIR/rpoS/bin/activate
    pip install -U pip
    cat $pydata | xargs -n 1 -L 1 pip install
    deactivate
}


setup_conda() {
    local conda_bin=$(which conda)
    if [ -z "$conda_bin" ];
    then
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
        chmod +x ./Miniconda3-latest-Linux-x86_64.sh
        ./Miniconda3-latest-Linux-x86_64.sh
        rm ./Miniconda3-latest-Linux-x86_64.sh
        source $HOME/.bashrc
    fi
    conda install nbformat
    conda config -add channels bioconda
    conda env create -f ../environment.yml
}


show_help() {
    cat <<EOF
    usage: $0 options

    Bootstraps a new ubuntu GNOME install to upgrade to the latest GNOME version, 
    setup most common dev dependencies, python stack, google browser and plugin, 
    and i3 windows manager.

    OPTIONS:

    -h | --help     display this help text and exit
    -d | --deps     install development and computational dependencies
    -c | --conda    set up conda environment
    -e | --env      set up python 3 virtualenv 
    -a | --all      all of the above
EOF
}

readonly OPTS=`getopt -o adech --long all,deps,env,conda,help -n 'bootstrap.sh' -- "$@"`

if [ $? != 0 ] ; then echo "Failed to parse options." >&2; exit 1; fi
eval set -- "$OPTS"

while true
do
    case "$1" in
        -a|--all)
            install_deps
            setup_env
            setup_conda
            shift
            ;;
        -d|--deps)
            install_deps
            shift
            ;;
        -e|--env)
            setup_env
            shift
            ;;
        -c|--conda)
            setup_conda
            shift
            ;;
        -h|--help)
            show_help
            shift
            ;;
        * )
            break
            ;;
    esac
done

