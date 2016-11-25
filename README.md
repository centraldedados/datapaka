# datapaka

    ___    ___
    \__\__/__/  Datapaka!
    | ._. |  |  Let's package this data!
    |_____|__| 
 
Datapaka is a command-line utility made to ease the process of creating
`datapackage.json` files by asking the user for the values to use.

[![asciicast](https://asciinema.org/a/92522.png)](https://asciinema.org/a/92522)


## Installation

You need to first install the dependencies:

    pip install -r requirements.txt
    
It's not needed, but rather useful to symlink the `datapaka` executable into
your PATH, so that you can run it from anywhere. In case your home directory
contains a `bin/` directory, some Linux distros like Debian already employ it
in their path.

    cd ~/bin
    ln -s ~/repos/datapaka .

Otherwise you can symlink it in `/usr/local/bin`, which requires root privileges:

    sudo ln -s ~/repos/datapaka/datapaka /usr/local/bin/datapaka


## Usage

Datapaka works inside the directory of your new data package. It will look for a 
`data/` directory inside and check its contents.

    cd new-data-package
    datapaka

In case you can't or don't want to follow the symlink suggestion above, you
need to call the `datapaka` script using its full path, e.g.

    cd new-data-package
    ~/repos/datapaka/datapaka
