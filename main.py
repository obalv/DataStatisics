from .config import Config
import requests, json, csv

querylist = {
	'userId': 'BCWH_BFJU_MDAA',
	'pwd': '52feiqiang',
	'interfaceId': 'getSurfEleByTimeRangeAndStaID',
	'dataCode': 'SURF_CHN_MUL_HOR',
	'dataFormat': 'json',
	'elements':[] 'Station_Id_C,Station_Id_d,Year,Mon,Day,Hour,TEM,PRE,WIN_D_Avg_2mi,WIN_S_Avg_2mi',
	'timeRange': '[20141231130000,20151231120000]',
	'staIds': '57469'
}

if __name__=='__main__':
	res = requests.get(Config.baseUrl, params=querylist)
	data = json.loads(res)
	if data['returnCode'] == str(0):
		for row in data['DS']:
