import requests, json, csv
from .utils import generatequerylist
from .config import Config

if __name__ == '__main__':
	querylist = generatequerylist('SURF_CHN_MUL_MON',
	                              'Station_Name,Station_Id_C,Year,Mon,Lat,Lon,Alti,WIN_S_Max,WIN_S_Inst_Max,WIN_S_2mi_Avg'
	                              , '[20151001000000,20170801000000]',
	                              '57469,Q6401,Q6402,Q6403,Q6404,Q6405,Q6406,Q6407,Q6408,Q6409,Q6410,Q6411,Q6412,Q6413,\
	                              Q6414,Q6415,Q6416,Q6417,Q6418,Q6419,Q6420,Q6421,Q6422,Q6423,Q6424,Q6425,Q6426')
	res = requests.get(Config.baseUrl, params=querylist)
	data = json.loads(res.text, strict=False)
	if data['returnCode'] == str(0):
		with open('feng.csv', 'w', newline='') as f:
			tablenames = Config.fieldnames
			writer = csv.DictWriter(f, fieldnames=tablenames)
			writer.writeheader()
			for row in data['DS']:
				for index in range(len(Config.fieldnames)):
					writer.writerow({
						Config.fieldnames[index]: row[index]
					})
	else:
		print('failed')
