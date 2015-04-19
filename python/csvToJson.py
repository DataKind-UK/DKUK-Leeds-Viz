import json
import csv
import sys


def main():
    csv_filename = sys.argv[1]
    json_filename = csv_filename[:-3] + 'json'

    tokens = csv_filename.split('/')
    variable_name = tokens[len(tokens) - 1]
    variable_name = variable_name[:-4]

    csv_file = open(csv_filename, 'r')
    json_file = open(json_filename, 'w')

    reader = csv.DictReader(csv_file)
    out = json.dumps([row for row in reader])
    json_file.write('{"' + variable_name + '":')
    json_file.write(out)
    json_file.write('}')

    csv_file.close()
    json_file.close()

if __name__ == '__main__':
    main()