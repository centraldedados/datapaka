from colorama import Style

'''
Remember to finish each line with a comma!
'''

prompts = {
    "title": [
        "What's the " + Style.BRIGHT + "title" + Style.RESET_ALL + " for this data package?",
        Style.DIM + "A title is a concise descriptor of what's in the data package, in human terms. 'Housing Prices in Berlin' or 'World Population Density' are good titles. (optional field)"],
    "slug": [
        "What's the " + Style.BRIGHT + "slug" + Style.RESET_ALL + " for this data package? [Leave blank for '%s']",  # %s is the default value
        Style.DIM + "A slug ('name' field) is a lower-case, no spaces version of the title. Use hyphens or underscores instead of spaces. 'berlin-housing-prices' or 'world-population-density' are good slugs."
    ],
    "slug_notitle": [  # Used when no title was specified - don't mention the default value
        "What's the " + Style.BRIGHT + "slug" + Style.RESET_ALL + " for this data package?",  # %s is the default value
        Style.DIM + "A slug ('name' field) is a lower-case, no spaces version of the title. Use hyphens or underscores instead of spaces. 'berlin-housing-prices' or 'world-population-density' are good slugs."
    ],
    "description": [
        "Give me a short, human " + Style.BRIGHT + "description" + Style.RESET_ALL + " for this data package.",
        Style.DIM + "A description gives more information about what's inside. 'Property prices in Berlin in April 2015' or 'UN population density statistics for the 2003-2013 period' let people know more specific details. Markdown formatting can be used. (optional field)"
    ],
    "version": [
        "What's the package " + Style.BRIGHT + "version number" + Style.RESET_ALL + "? [Leave blank for '%s']",
        Style.DIM + "The version number tracks changes and improvements on the data package.",
        "If you're starting a new one, go with the default value of 0.1.0, and update it whenever there is a change in the data layout."
    ],
    "homepage": [
        "What's the " + Style.BRIGHT + "homepage" + Style.RESET_ALL + " for this data package?",
        Style.DIM + "Please include the 'http://' prefix. (optional field)"
    ],
    "license_options": {
        "1": "ODC-PDDL-1.0",
        "2": "ODbL-1.0",
        "3": "ODC-BY-1.0",
        "4": "CC0-1.0",
        "5": "CC-BY-4.0",
        "6": "CC-BY-SA-4.0",
    },
    "license": [
        "What's the package " + Style.BRIGHT + "license" + Style.RESET_ALL + "? [Leave blank for '%s'] ",
        Style.DIM + "The license field states the license under which this package is to be published. Read more about each license at http://opendefinition.org/licenses/.",
        '1) Public Domain Dedication and License (public domain)',
        '2) Open Database License (attribution, sharealike)',
        '3) Open Data Commons Attribution License (attribution)',
        '4) Creative Commons Zero (public domain)',
        '5) Creative Commons Attribution',
        '6) Creative Commons Attribution-ShareAlike',
    ],
    "sources_intro": [
        "Now I want to know about the " + Style.BRIGHT + "sources" + Style.RESET_ALL + " of your data.",
        Style.DIM + "I will ask you the name and URL for each, and then you'll be asked if you want to input another source or move ahead."
    ],
    "contributors_intro": [
        "Now I want to know about the " + Style.BRIGHT + "contributors" + Style.RESET_ALL + " of this data package.",
        Style.DIM + "I will ask you the name, e-mail and website URL for each, and then you'll be asked if you want to input another contributor or move ahead."
    ],
    "keywords": [
        "Tell me some " + Style.BRIGHT + "keywords" + Style.RESET_ALL + " (tags) for this package so that users can find it in catalogs. [optional]",
        Style.DIM + "Keywords can have spaces; separate distinct keywords with commas."

    ],
}
