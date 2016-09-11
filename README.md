# datapaka

    ___    ___
    \__\__/__/  Datapaka!
    | ._. |  |  Let's package this data!
    |_____|__| 
 
Datapaka is a command-line utility made to ease the process of creating
`datapackage.json` files by asking the user for the values to use.

It's still very bare-bones, but can already be used to bootstrap data packages.


## Installation

You need to first install the dependencies:

    pip install -r requirements.txt
    
It's not needed, but rather useful to symlink the `datapaka` executable into
your PATH, so that you can run it from anywhere. In case your home directory
contains a `bin/` directory, some Linux distros like Debian already employ it
in their path.

    cd ~/bin
    ln -s ~/repos/datapaka .

Otherwise you can symlink it in `/usr/bin` which is probably overkill:

    sudo ln -s ~/repos/datapaka/datapaka /usr/bin/datapaka


## Usage

Datapaka works inside the directory of your new data package. 

    cd new-data-package
    datapaka

In case you can't or don't want to follow the symlink suggestion above, you
need to call the `datapaka` script using its full path, e.g.

    cd new-data-package
    ~/repos/datapaka/datapaka


## TODO

* Finish the UI with the CSV column naming and final output
* Arguments!
  - create blank datapackage.json without interaction, guessing values where reasonable
  - validate existing datapackage.json using the `datapackage` module
  - overwrite existing datapackage.json
* When present, read existing datapackage.json and use its values as the default
* Employ OrderedDict so that the output can be predictable and thus diff-able

