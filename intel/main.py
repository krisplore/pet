#!venv/bin/python
import sys
from getopt_router import getopt_entity_action
from source.add import add as source_add


def main():
    args_entity_action = getopt_entity_action()
    entity = args_entity_action[0]
    # action = args_entity_action[1]

    match entity:
        case 'source':
            source_add()
        case _:
            print('no')


if __name__ == "__main__":
    main()
