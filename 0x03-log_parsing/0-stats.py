#!/usr/bin/python3
"""Scripts that reads stdin line by line and computes metrics"""

import sys

total_size = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}
counter = 0

try:
    for line in sys.stdin:
        line_split = line.split(" ")
        if len(line_split) > 4:
            code = line_split[-2]
            size = int(line_split[-1])
            if code in status_codes.keys():
                status_codes[code] += 1
            total_size += size
            counter += 1

            if counter == 10:
                print('File size: {}'.format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                counter = 0

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
