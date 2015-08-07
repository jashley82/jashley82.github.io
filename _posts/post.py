#!/usr/bin/env python

import argparse
import arrow

parser = argparse.ArgumentParser()
parser.add_argument('title', help='title of post', type=str)

args = parser.parse_args()
now = arrow.now().format('YYYY-M-D')

filename = '{}-{}.md'.format(now, args.title.replace(' ', '-'))
fh = open('{}'.format(filename), 'w')

fh.write('---')
fh.write('\n')
fh.write('layout: post')
fh.write('\n')
fh.write('title: {}'.format(args.title))
fh.write('\n')
fh.write('---')
fh.write('\n')
fh.write('\n')

fh.close()
