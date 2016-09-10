# datapaka

    ___    ___
    \__\__/__/  Datapaka!
    | ._. |  |  Let's package this data!
    |_____|__| 
 
Datapaka is a command-line utility made to ease the process of creating `datapackage.json` files by asking the user for the values to use.

It's still very bare-bones, but can already be used to bootstrap data packages.

## Installation

You need to first install the dependencies:

    pip install -r requirements.txt
    
## Usage

It's useful to symlink the `datapaka` executable into your PATH, so that you can run it from anywhere.

Just run `datapaka` inside the directory of the data package you're creating.

If you can't or don't want to follow the symlink suggestion above, you need to call the `datapaka` script using its full path, e.g.

    ~/repos/datapaka/datapaka
    
## TODO

* Employ OrderedDict so that the output can be predictable
* Use color in the output

