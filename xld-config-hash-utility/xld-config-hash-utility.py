# Run as python xld-config-hash-utility.py log1.log log2.log
# Configure xld-config-hash-utility.properties file in this way:
# [CommonSection]
# datetime_pattern=([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3})
# hash_pattern=Using hash ([0-9a-f]{64}) for (\S+)
#
# [Log1Section]
# start_datetime=2020-02-05 00:00:00.000
# end_datetime=2020-02-05 23:59:59.999
#
# [Log2Section]
# start_datetime=2020-02-05 00:00:00.000
# end_datetime=2020-02-05 23:59:59.999
#

import re
import sys
import ConfigParser

def create_map(pattern, log_file_path, key_hash_map, start_datetime, end_datetime):
    line_count = 0
    matched_line_count = 0
    log_file = open(log_file_path)
    for line in log_file:
        line_count += 1
        m = pattern.match(line)
        if m:
            matched_line_count += 1
            if m.group(1) >= start_datetime and m.group(1) <= end_datetime:
                key_hash_map[m.group(3)] = m.group(2)
    log_file.close()
    print "Read %s lines from %s" % (line_count, log_file_path)
    print "Processing %s hashed items from %s" % (matched_line_count, log_file_path)

def compare_maps(key_hash_map_1, key_hash_map_2):
    print "Match %d items in left log to right log\n" % len(key_hash_map_1)
    for key in key_hash_map_1.keys():
        if key in key_hash_map_2.keys():
            if key_hash_map_1[key] == key_hash_map_2[key]:
                continue
            else:
                print "Mismatch on item %s:\nleft file hash is  %s\nright file hash is %s\n" % (key, key_hash_map_1[key], key_hash_map_2[key])
        else:
            print "Mismatch on item %s in left file but not in right file\n" % key

config = ConfigParser.RawConfigParser()
config.read('xld-config-hash-utility.properties')

datetime_pattern = config.get('CommonSection', 'datetime_pattern')
hash_pattern = config.get('CommonSection', 'hash_pattern')
pattern = re.compile(datetime_pattern + ".*" + hash_pattern + ".*")

log1_map = {}
log2_map = {}
divider = config.get('CommonSection', 'divider_char') * int(config.get('CommonSection', 'divider_length')) + "\n"
print ""
create_map(pattern, sys.argv[1], log1_map, config.get('Log1Section', 'start_datetime'), config.get('Log1Section', 'end_datetime'))
print ""
create_map(pattern, sys.argv[2], log2_map, config.get('Log1Section', 'start_datetime'), config.get('Log1Section', 'end_datetime'))
print "\n" + divider
print "Compare %s (left) to %s (right)" % (sys.argv[1], sys.argv[2])
compare_maps(log1_map, log2_map)
print divider
print "Compare %s (left) to %s (right)" % (sys.argv[2], sys.argv[1])
compare_maps(log2_map, log1_map)
print divider
print "Execution completed"
