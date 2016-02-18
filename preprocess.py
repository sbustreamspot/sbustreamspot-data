# Copyright 2016 Emaad Ahmed Manzoor
# License: Apache License, Version 2.0
# https://github.com/sbustreamspot/sbustreamspot-data/

import sys

map = {'process': 'a',
       'thread': 'b',
       'file': 'c',
       'MAP_ANONYMOUS': 'd',
       'NA': 'e',
       'stdin': 'f',
       'stdout': 'g',
       'stderr': 'h',
       'accept': 'i',
       'access': 'j',
       'bind': 'k',
       'chmod': 'l',
       'clone': 'm',
       'close': 'n',
       'connect': 'o',
       'execve': 'p',
       'fstat': 'q',
       'ftruncate': 'r',
       'listen': 's',
       'mmap2': 't',
       'open': 'u',
       'read': 'v',
       'recv': 'w',
       'recvfrom': 'x',
       'recvmsg': 'y',
       'send': 'z',
       'sendmsg': 'A',
       'sendto': 'B',
       'stat': 'C',
       'truncate': 'D',
       'unlink': 'E',
       'waitpid': 'F',
       'write': 'G',
       'writev': 'H',
      }

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        prev_src_id = ""
        prev_dst_id = ""
        prev_e_type = ""
        prev_graph_id = ""
        for line in f:
            fields = [w.strip() for w in line.split(',')]
            fields[0] = str(int(fields[0]) + 1)
            fields[1] = map[fields[1]]
            fields[2] = str(int(fields[2]) + 1)
            fields[3] = map[fields[3]]
            fields[4] = map[fields[4]]

            # avoid parallel edges from block-based file reads
            if fields[0] == prev_src_id and\
               fields[2] == prev_dst_id and\
               fields[4] == prev_e_type and\
               fields[6] == prev_graph_id:
                continue
            prev_src_id = fields[0]
            prev_dst_id = fields[2]
            prev_e_type = fields[4]
            prev_graph_id = fields[6]

            del fields[5] # no timestamp
            print '\t'.join(fields)
