#!/usr/bin/python3

import re

SRC      = './contracts/templates'
DST      = './contracts/libs'
PATTERNS = './patterns.txt'

FORMAT = {
	'LibSet': [ 'VALUE' ],
	'LibMap': [ 'KEY', 'VALUE' ],
}

TYPES = {
	'bool':    { 'reference': False },
	'int8':    { 'reference': False },
	'int16':   { 'reference': False },
	'int24':   { 'reference': False },
	'int32':   { 'reference': False },
	'int40':   { 'reference': False },
	'int48':   { 'reference': False },
	'int56':   { 'reference': False },
	'int64':   { 'reference': False },
	'int72':   { 'reference': False },
	'int80':   { 'reference': False },
	'int88':   { 'reference': False },
	'int96':   { 'reference': False },
	'int104':  { 'reference': False },
	'int112':  { 'reference': False },
	'int120':  { 'reference': False },
	'int128':  { 'reference': False },
	'int136':  { 'reference': False },
	'int144':  { 'reference': False },
	'int152':  { 'reference': False },
	'int160':  { 'reference': False },
	'int168':  { 'reference': False },
	'int176':  { 'reference': False },
	'int184':  { 'reference': False },
	'int192':  { 'reference': False },
	'int200':  { 'reference': False },
	'int208':  { 'reference': False },
	'int216':  { 'reference': False },
	'int224':  { 'reference': False },
	'int232':  { 'reference': False },
	'int240':  { 'reference': False },
	'int248':  { 'reference': False },
	'int256':  { 'reference': False },
	'uint8':   { 'reference': False },
	'uint16':  { 'reference': False },
	'uint24':  { 'reference': False },
	'uint32':  { 'reference': False },
	'uint40':  { 'reference': False },
	'uint48':  { 'reference': False },
	'uint56':  { 'reference': False },
	'uint64':  { 'reference': False },
	'uint72':  { 'reference': False },
	'uint80':  { 'reference': False },
	'uint88':  { 'reference': False },
	'uint96':  { 'reference': False },
	'uint104': { 'reference': False },
	'uint112': { 'reference': False },
	'uint120': { 'reference': False },
	'uint128': { 'reference': False },
	'uint136': { 'reference': False },
	'uint144': { 'reference': False },
	'uint152': { 'reference': False },
	'uint160': { 'reference': False },
	'uint168': { 'reference': False },
	'uint176': { 'reference': False },
	'uint184': { 'reference': False },
	'uint192': { 'reference': False },
	'uint200': { 'reference': False },
	'uint208': { 'reference': False },
	'uint216': { 'reference': False },
	'uint224': { 'reference': False },
	'uint232': { 'reference': False },
	'uint240': { 'reference': False },
	'uint248': { 'reference': False },
	'uint256': { 'reference': False },
	'bytes1':  { 'reference': False },
	'bytes2':  { 'reference': False },
	'bytes3':  { 'reference': False },
	'bytes4':  { 'reference': False },
	'bytes5':  { 'reference': False },
	'bytes6':  { 'reference': False },
	'bytes7':  { 'reference': False },
	'bytes8':  { 'reference': False },
	'bytes9':  { 'reference': False },
	'bytes10': { 'reference': False },
	'bytes11': { 'reference': False },
	'bytes12': { 'reference': False },
	'bytes13': { 'reference': False },
	'bytes14': { 'reference': False },
	'bytes15': { 'reference': False },
	'bytes16': { 'reference': False },
	'bytes17': { 'reference': False },
	'bytes18': { 'reference': False },
	'bytes19': { 'reference': False },
	'bytes20': { 'reference': False },
	'bytes21': { 'reference': False },
	'bytes22': { 'reference': False },
	'bytes23': { 'reference': False },
	'bytes24': { 'reference': False },
	'bytes25': { 'reference': False },
	'bytes26': { 'reference': False },
	'bytes27': { 'reference': False },
	'bytes28': { 'reference': False },
	'bytes29': { 'reference': False },
	'bytes30': { 'reference': False },
	'bytes31': { 'reference': False },
	'bytes32': { 'reference': False },
	'address': { 'reference': False },
	'string':  { 'reference': True  },
	'bytes':   { 'reference': True  },
}

def process(entry):
	try:
		m      = re.search('^(.+)<(.+)>$', entry)
		type   = m.group(1)
		args   = m.group(2).split(',')
		code   = open('{}/{}.sol.templated'.format(SRC, type), 'r').read()
		target = '{}/{}.{}.sol'.format(DST, type, '.'.join(args))

		for (key, type) in zip(FORMAT[type], args):
			code = code.replace('<{}>'.format(key), type)
			code = code.replace('<{}_LOCATION>'.format(key), 'memory' if TYPES[type]['reference'] else '')

		open(target, 'w').write(code)
		print('→ {} generated'.format(target))
	except:
		print('Error: invalid pattern `{}`'.format(entry))

if __name__ == '__main__':
	with open(PATTERNS) as file:
		for line in file:
			process(line[:-1])
