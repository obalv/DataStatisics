from config import Config
import requests, json, csv

querylist = {
	'userId': 'BCWH_BFJU_MDAA',
	'pwd': '52feiqiang',
	'interfaceId': 'getSurfEleByTimeRangeAndStaID',
	'dataCode': 'SURF_CHN_MUL_DAY',
	'dataFormat': 'json',
	'elements': 'Station_Id_C,Year,Mon,Day,PRS_Avg,WIN_S_Inst_Max,WIN_D_INST_Max,TEM_Avg,RHU_Avg,PRE_Time_2020,WEP_Record',
	'timeRange': '[20150101000000,20170906000000]',
	'staIds': '57469'
}

if __name__ == '__main__':
	res = requests.get(Config.baseUrl, params=querylist)
	data = json.loads(res.text)
	print(data)
	# if data['returnCode'] == str(0):
	# 	with open('weishui.csv', 'w', newline='') as f:
	# 		tablenames = Config.fieldnames
	# 		writer = csv.DictWriter(f, fieldnames=tablenames)
	# 		writer.writeheader()
	# 		for row in data['DS']:
	# 			writer.writerow({
	# 				Config.fieldnames[0]: row['Station_Id_C'],
	# 				Config.fieldnames[1]: row['Year'],
	# 				Config.fieldnames[2]: row['Mon'],
	# 				Config.fieldnames[3]: row['Day'],
	# 				Config.fieldnames[4]: row['PRS_Avg'],
	# 				Config.fieldnames[5]: row['TEM_Avg'],
	# 				Config.fieldnames[6]: row['PRE_Time_2020'],
	# 				Config.fieldnames[7]: row['RHU_Avg'],
	# 				Config.fieldnames[8]: row['WIN_S_Inst_Max'],
	# 				Config.fieldnames[9]: str(int(row['WIN_D_INST_Max'])-999000),
	# 				Config.fieldnames[10]: row['WEP_Record']
	# 			})
	# else:
	# 	print('failed')