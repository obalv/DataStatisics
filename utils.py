from .config import Config

WindCoverter = {

}
Dirs = {
	1: 'N',
	2: 'NNE',
	3: 'NE',
	4: 'ENE',
	5: 'E',
	6: 'ESE',
	7: 'SE',
	8: 'SSE',
	9: 'S',
	10: 'SSW',
	11: 'SW',
	12: 'WSW',
	13: 'W',
	14: 'WNW',
	15: 'NW',
	16: 'NNW'
}


def initializequeryparams(**kwargs):
	pass


# def convertwinddir(s):
# 	if int(s) > 10000:
# 		_s = int(s) - 999000
# 		return Dirs.get(_s, 'C')

def generatequerylist(datacode, elements, timerange, staids):
	querylist = {}
	querylist['dataCode'] = datacode
	querylist['elements'] = elements
	querylist['timeRange'] = timerange
	querylist['staIds'] = staids
	return querylist
