import json, csv
from collections import OrderedDict
from bottle import get, run, response


def loadData(file):
	ldfile = open(file)
	allData = csv.DictReader(ldfile)
	return allData


dem_file = 'dem_results.csv'
rep_file = 'rep_results.csv'


def getUnique_fips():
	demFile = loadData(dem_file)
	unique_fips = set()
	for t_row in demFile:
		unique_fips.add(t_row["fips"])
	return sorted(unique_fips)


def getUnique_fips_counties():
	data = open(dem_file)
	next(data, None)
	demFile1 = list(csv.reader(data))
	unique_fips = getUnique_fips()
	unique_fips_county = []
	for u_fips in unique_fips:
		for tt_row in demFile1:
			if u_fips == tt_row[1]:
				unique_fips_county.append({'county':tt_row[0], 'fips':tt_row[1]})
				break
	return unique_fips_county


def repCounties(t_fips):
	repFile = loadData(rep_file)
	rep_resultList = []
	for row in repFile:
		if t_fips == row["fips"]:
			repDict = OrderedDict()
			repDict["candidate"] = row["candidate"]
			repDict["votes"] = row["votes"]
			rep_resultList.append(repDict)
	return rep_resultList


def demCounties(t_fips):
	demFile = loadData(dem_file)
	dem_resultList = []
	for row in demFile:
		if t_fips == row["fips"]:
			demDict = OrderedDict()
			demDict["candidate"] = row["candidate"]
			demDict["votes"] = row["votes"]
			dem_resultList.append(demDict)
	return dem_resultList


#@get('/counties')
def rep_demCounties():
	unique_fips_county = getUnique_fips_counties()
	output = {}
	outputList = []

	for row in unique_fips_county:
		countiesDict = OrderedDict()
		countiesDict["name"] = row["county"]
		countiesDict["fips"] = row["fips"]
		dem_resultList = demCounties(row["fips"])
		rep_resultList = repCounties(row["fips"])
		countiesDict["elections"] = [{"party": "Democratic", "results":dem_resultList},{"party": "Republican", "results": rep_resultList}]
		outputList.append(countiesDict)

	output["counties"] = outputList
	response.content_type = 'application/json'

	return json.dumps(output, indent=2)

#rep_demCounties()


@get('/counties/<fips>')
def get_fips(fips):
	unique_fips_county = getUnique_fips_counties()
	output = {}
	outputList = []
	val = str(fips)

	for row in unique_fips_county:
		if row["fips"] == val:
			countiesDict = OrderedDict()
			countiesDict["name"] = row["county"]
			countiesDict["fips"] = row["fips"]
			dem_resultList = demCounties(val)
			rep_resultList = repCounties(val)
			countiesDict["elections"] = [{"party": "Democratic", "results":dem_resultList},{"party": "Republican", "results": rep_resultList}]
			outputList.append(countiesDict)
	output["counties"] = outputList
	response.content_type = 'application/json'

	return json.dumps(output, indent=2)

get_fips(19005)

run(host='localhost', port=8080)