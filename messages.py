from colorama import Style, Fore

'''
Remember to finish each line with a comma!
'''

# colorama shortcuts
BRIGHT = Style.BRIGHT
DIM = Style.DIM
RESET = Style.RESET_ALL

messages = {
    "title": [
        "What's the " + BRIGHT + "title" + RESET + " for this data package?",
        DIM + "A title is a concise descriptor of what's in the data package, in human terms. 'Housing Prices in Berlin' or 'World Population Density' are good titles. (optional field)"],
    "slug": [
        "What's the " + BRIGHT + "slug" + RESET + " for this data package? [Leave blank for '%s']",  # %s is the default value
        DIM + "A slug ('name' field) is a lower-case, no spaces version of the title. Use hyphens or underscores instead of spaces. 'berlin-housing-prices' or 'world-population-density' are good slugs."
    ],
    "slug_notitle": [  # Used when no title was specified - don't mention the default value
        "What's the " + BRIGHT + "slug" + RESET + " for this data package?",  # %s is the default value
        DIM + "A slug ('name' field) is a lower-case, no spaces version of the title. Use hyphens or underscores instead of spaces. 'berlin-housing-prices' or 'world-population-density' are good slugs."
    ],
    "description": [
        "Give me a short, human " + BRIGHT + "description" + RESET + " for this data package.",
        DIM + "A description gives more information about what's inside. 'Property prices in Berlin in April 2015' or 'UN population density statistics for the 2003-2013 period' let people know more specific details. Markdown formatting can be used. (optional field)"
    ],
    "version": [
        "What's the package " + BRIGHT + "version number" + RESET + "? [Leave blank for '%s']",
        DIM + "The version number tracks changes and improvements on the data package.",
        DIM + "If you're starting a new one, go with the default value of %s, and update it whenever there is a change in the data layout."
    ],
    "homepage": [
        "What's the " + BRIGHT + "homepage" + RESET + " for this data package?",
        DIM + "Please include the 'http://' prefix. (optional field)"
    ],
    "license": [
        "What's the package " + BRIGHT + "license" + RESET + "? [Leave blank for '%s'] ",
        DIM + "The license field states the license under which this package is to be published. Read more about each license at http://opendefinition.org/licenses/.",
        '1) Public Domain Dedication and License (public domain)',
        '2) Open Database License (attribution, sharealike)',
        '3) Open Data Commons Attribution License (attribution)',
        '4) Creative Commons Zero (public domain)',
        '5) Creative Commons Attribution',
        '6) Creative Commons Attribution-ShareAlike',
    ],
    "sources_intro": [
        "Now I want to know about the " + BRIGHT + "sources" + RESET + " of your data.",
        DIM + "I will ask you the name and URL for each, and then you'll be asked if you want to input another source or move ahead."
    ],
    "contributors_intro": [
        "Now I want to know about the " + BRIGHT + "contributors" + RESET + " of this data package.",
        DIM + "I will ask you the name, e-mail and website URL for each, and then you'll be asked if you want to input another contributor or move ahead."
    ],
    "keywords": [
        "Tell me some " + BRIGHT + "keywords" + RESET + " (tags) for this package so that users can find it in catalogs. [optional]",
        DIM + "Keywords can have spaces; separate distinct keywords with commas."
    ],

    "error_nodatadir": [
        "The data/ directory does not exist, can't do much here.",
        "Please create it and place some CSV files inside, then call me again."
        ""
    ],
    "info_exists": [
        "There already is a datapackage.json file here.",
        "I will save the result of this in " + BRIGHT + "datapackage-new.json" + RESET + ".",
        ""
    ],
    "required_field": [
        "This field is required!",
    ],
    "question_prompt": Style.BRIGHT + "? ",
    "done": [
        "All done! File saved as " + BRIGHT + "%s" + RESET + ". Ta!",
    ],

    "splash": [  # Initial "splash screen"
        "",
        Fore.YELLOW + "   ___    ___  ",
        Fore.YELLOW + "   \__\__/__/  " + Fore.RESET + "Datapaka!",
        Fore.YELLOW + "   | ._. |  |  " + Fore.RESET + "Let's package this data!",
        Fore.YELLOW + "   |_____|__|  ",
        ""
    ],
}

license_options = {
    "1": "ODC-PDDL-1.0",
    "2": "ODbL-1.0",
    "3": "ODC-BY-1.0",
    "4": "CC0-1.0",
    "5": "CC-BY-4.0",
    "6": "CC-BY-SA-4.0",
}


def print_message(name, format_strings=None):
    '''Print the prompt messages according to the list in prompts.py.'''
    print("")
    for line in messages[name]:
        if format_strings and ("%s" in line or "%d" in line):
            print(line % format_strings)
        else:
            print(line)
