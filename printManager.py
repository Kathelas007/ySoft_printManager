#!/usr/bin/env python3

import sys
import json


def help():
    print("""\nAplication stores data in JSON format to output file and prints on stdout sum of letters. 
    Script expects 4 arguments:
            username - string
            printer name - string
            path to input file with data
            path to output file in JSON format""")


def check_args():
    if len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-help"):
        help()
        sys.exit(0)

    if len(sys.argv) != 5:
        print("Bad number of arguments.")
        help()
        sys.exit(1)


def get_input_data(path_in):
    try:
        in_file = open(path_in, 'r')
        in_data = in_file.read()
        in_file.close()
        return in_data

    except FileNotFoundError:
        print("Cant find input file")
        help()
        sys.exit(1)
    except IOError:
        print("Cant read input file")
        in_file.close()
        help()
        sys.exit(1)


def write_json_to_file(json_data, path_out):
    try:
        out_file = open(path_out, 'w')
        json.dump(json_data, out_file)
        out_file.close()

    except FileNotFoundError:
        print("Cant find output file")
        help()
        sys.exit(1)


def get_json_data(user_name, printer_name, in_data):
    return {"userName": user_name, "printerName": printer_name, "data": in_data}


def get_stdout_data(in_data):
    stdout_data = {letter: in_data.count(letter) for letter in sorted(set(in_data.lower()))
                   if  letter.isalpha() and not letter.isspace()}

    return '\n'.join("{}: {}".format(k, v) for k, v in stdout_data.items())


def print_data(user_name, printer_name, path_in, path_out):

    in_data = get_input_data(path_in)

    """first part, write to output file in json format"""
    json_data = get_json_data(user_name, printer_name, in_data)
    write_json_to_file(json_data, path_out)

    """second part, input data to stdout"""
    stdout_data = get_stdout_data(in_data)
    print(stdout_data)

if __name__ == "__main__":
    check_args()
    print_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
