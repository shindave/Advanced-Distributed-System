__author__ = 'wangyijun'
import sqlite3
import sys
from collections import  defaultdict

fileLists = ['fp_dis.sqlite', 'fp_pb.sqlite']
baseline = 'fourthparty.sqlite'
baseline_map = dict()


def main():
    global fileLists
    global baseline
    global fileLists
    conn = sqlite3.connect(baseline)
    c = conn.cursor()
    c.execute('select request_origin, content_location from content_policy')
    rows = c.fetchall()
    for row in rows:
        baseline_map[row[1]] = 1
    conn.close()

    for filename in fileLists:
        temp_map = dict()
        temp_conn = sqlite3.connect(filename)
        tc = temp_conn.cursor()
        tc.execute('select request_origin, content_location from content_policy')
        t_rows = tc.fetchall()
        for row in t_rows:
            temp_map[row[1]] = 1
        savefile = filename.split('.')[0] + '.txt'
        wp = open(savefile, 'w')
        count = 0
        for key in baseline_map.keys():
            if key not in temp_map.keys():
                count += 1
                wp.write(key + '\n')
        wp.write(str(float(count)/len(baseline_map.keys())) + '\n')
        wp.close()
        temp_conn.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    sys.exit()