# -*- coding: utf-8 -*-
import sys
import requests
import codecs
import re
variable = 'coordsB'

# sys.stdin = open('a.dat')
# sys.stdin = codecs.getreader("utf-8")(sys.stdin)

fin = codecs.open('0.dat', encoding='utf-8')

outfile = codecs.open('out.txt', 'w', encoding='utf-8')

lines = fin.readlines()
lastStreet = ""
lastBuilding = ""

archive = []

def isDigit(str):
	return len(str)==1 and str[0] in ['1','2','3','4','5','6','7','8','9','0']

def isBuildingNumber(str):
	return isDigit(str[0])

def trimBuildingNumber(str):
	res = ""
	i = 0
	while str and isDigit(str[0]):
		res += str[0]
		str = str[1:]
	return res


def getcoo(address):
	# return '1 1'
	# print u'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=Харьков,' + address
	r = requests.get(u'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=Харьков,' + address)
	res = r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].strip()
	return res


# def str:
# 	return str.decode('cp1251').encode('utf-8')

outfile.write('var ' + variable + ' = [\n')

cnt = 0
lastType = ""
for line in lines:
	line = re.sub(u'п.[1-9]','',line)

	line = line.strip().replace(u'Ж.д.(частный сектор):', ',')
	line = line.strip().replace(u'ж.дом','')
	line = line.strip().replace(u'ж.д','')
	line = line.strip().replace(u'№','')
	line = line.strip().replace(u'—', '-')
	line = line.strip().replace(' - ',' , ')
	line = line.strip().replace(';',',')
	line = line.strip().replace('  ',',')


	components = line.split(",")

	for comp in components:
		print cnt
		cnt += 1
		comp = comp.strip()
		# re.sub('[0-9] ','',comp)
		comp = re.sub(u'([0-9]) ([а-я])$',r'\1\2',comp)
		comp = re.sub(u'([0-9])-([а-я])$',r'\1\2',comp)

		if len(comp):
			# print comp, len(comp), isDigit(comp)
			if len(comp) == 1 and not isDigit(comp):
				res = lastStreet + ' ' + lastBuilding + ' ' + comp
				lastType = "letter";
			elif isBuildingNumber(comp):
				lastBuilding = trimBuildingNumber(comp)
				res = lastStreet + ' ' + comp
				lastType = "building"
			# elif not isBuildingNumber(comp):
			elif len(comp)<=6:
				lastBuilding = comp
				res = lastStreet + ' ' + comp
				lastType = "building"
			else:
				parts = comp.split(' ')
				if len(parts) > 1 and isBuildingNumber(parts[-1]):
					lastStreet = " ".join(parts[:-1])
					lastBuilding = trimBuildingNumber(parts[-1])
					lastType = "building";
					res = lastStreet + ' ' + parts[-1]
				else:
					if lastType == "street":
						res = lastStreet
					else:
						res = None
					lastStreet = comp
					lastType = "street"

			if res:
				res = re.sub(u'([0-9]) ([а-я])$',r'\1\2',res)
				res = re.sub(u'([0-9])-([а-я])$',r'\1\2',res)
				coo = getcoo(res)
				# print 'coo', coo
				if coo not in archive:
					archive.append(coo)
					coo = coo.split()
					outfile.write('\t["' + res + '", ' + coo[1] + ', ' + coo[0] + '],' + ' \n')

outfile.write(']\n')