"""
Responsible for managing the process of adding a new source.
"""

import sys              #
from intel.source.input_data import parse_options, parse_filename
from intel.source.functions import create_source_stub, \
    print_source_information, validator
from intel.source.yaml_functions import save_to_yaml
from intel.definitions import PATH_BASE, SOURCE_EXTENSION_YAML, NAME_PROJECT
from intel.source.input_data import parse_input_method
from intel.source.yaml_functions import read_from_yaml
from intel.translation import start_translating

PATH_TO_LOCALES: str = PATH_BASE + '/locales'
PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'
_ = start_translating()


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """

    print(_("Language"))

    source = create_source_stub()

    input_method = parse_input_method()

    match input_method:
        case 'file':
            raw_source = read_from_yaml(parse_filename(sys.argv[4:]))
        case 'opt':
            raw_source = parse_options(sys.argv[4:])
        case _:
            print(_('Method does not exist'))
            sys.exit(2)

    success = validator(raw_source)

    if not success['status']:
        print_source_information(success['errors'])
        sys.exit(2)
    else:
        print_source_information(success)
        source.update(raw_source)

        save_to_yaml(source, PATH_TO_STORAGE + source['id'] + SOURCE_EXTENSION_YAML)
        print_source_information(source)
