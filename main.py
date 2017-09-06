from .config import Config
import requests, json, csv

querylist = {
	'userId': 'BCWH_BFJU_MDAA',
	'pwd': '52feiqiang',
	'interfaceId': 'getSurfEleByTimeRangeAndStaID',
	'dataCode': 'SURF_CHN_MUL_HOR',
	'dataFormat': 'json',
	'elements': 'Station_Id_C,Year,Mon,Day,PRS_Avg,WIN_S_Inst_Max,WIN_D_INST_Max,TEM_Avg,RHU_Avg,PRE_Time_2020,WEP_Record',
	'timeRange': '[20141231130000,20151231120000]',
	'staIds': '57469'
}

if __name__ == '__main__':
	res = requests.get(Config.baseUrl, params=querylist)
	data = json.loads(res)
	if data['returnCode'] == str(0):
		for row in data['DS']:
			with open('weishui.csv', 'w') as f:
				tablenames = ['区站号', '年', '月', '日', '时', '温度', '降水', '两分钟平均风向', '两分钟平均风速']
				writer = csv.DictWriter(f, fieldnames=tablenames)
				writer.writeheader()
