# encoding=utf8
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')

sys.stdin = open('svet')
outfile = open('out.txt', 'w')

lines = sys.stdin.readlines()
first = ""

def getcoo(address):
	r = requests.get(u'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=Харьков,' + address)
	return r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

cnt = 0
for line in lines:
	print cnt
	cnt += 1
	line = line.strip()
	components = line.split(",")
	if len(components) > 1 and components[1]:
		for comp in components:
			comp = comp.strip()
			if comp.startswith('1') or comp.startswith('2') or comp.startswith('3') or comp.startswith('4') or comp.startswith('5') or comp.startswith('6') or comp.startswith('7') or comp.startswith('8') or comp.startswith('9'):
				res = first + ', ' + comp
				outfile.write(res + '/////' + getcoo(res) + '\n')
			else:
				while comp.endswith('0') or comp.endswith('1') or comp.endswith('2') or comp.endswith('3') or comp.endswith('4') or comp.endswith('5') or comp.endswith('6') or comp.endswith('7') or comp.endswith('8') or comp.endswith('9'):
					comp = comp[:-1].strip()
				comp = comp.split(' ')
				if len(comp) > 1 and '1' not in comp[1] and '2' not in comp[1] and  '3' not in comp[1] and  '4' not in comp[1] and  '5' not in comp[1] and  '6' not in comp[1] and  '7' not in comp[1] and  '8' not in comp[1] and '9' not in comp[1]:
					comp = comp[0] + ' ' + comp[1]
				else:
					comp = comp[0]
				first = comp
	elif len(line)>4:
		res = line
		outfile.write(res + '/////' + getcoo(res) + '\n')
	# if components[0].startswith(u'ул.') and components[0].startswith(u'пр.') or components[0].startswith(u'пер.') or components[0].startswith(u'в-зд') or components[0].startswith(u'пр-зд'):
	# 	first = components[0]

	# if len(line) < 5 or line.startswith('1') or line.startswith('2') or line.startswith('3') or line.startswith('4') or line.startswith('5') or line.startswith('6') or line.startswith('7') or line.startswith('8') or line.startswith('9'):
	# 	sys.stdout.write(first + ', ' + line)
	# 	sys.stdout.write('\n')
	# elif len(components) > 2:
	# 	for c in components[1:]:
	# 		sys.stdout.write(first + ', ' + c)
	# 		sys.stdout.write('\n')
	# else:
	# 	sys.stdout.write(line)
	# 	sys.stdout.write('\n')