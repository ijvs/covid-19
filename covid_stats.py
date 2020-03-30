import requests
import json 
import re
from datetime import date

class DataToJson:
	"""Class to convert government data format to beatiful JSON"""
	def __init__(this):
		this.url_mapa = "http://ncov.sinave.gob.mx/mapa45.aspx"
		this.req = requests.get(this.url_mapa)
		this.headers = {"Content-Type":"application/json; charset=utf-8"}
			
	def get_date_label(this):
		"""Get info label about last updete"""
		try:
			return re.findall(r'(Cierre con corte.+?)";',this.req.text)[-1]
		except Exception as e:
			return ""

	def get_source_file_number(this):
		"""Get name of the source file"""
		try:
			return re.findall(r'Mapa45.aspx\/(.+?)",',this.req.text)[0]
		except Exception as e:
			return ""		

	def get_stats(this):
		"""Return the formated data"""
		url = "http://ncov.sinave.gob.mx/Mapa45.aspx/"+this.get_source_file_number()
		req = requests.post(url, data={}, headers= this.headers)
		
		raw_data = json.loads(req.text)["d"]
		result = json.loads(raw_data)
		update_label = this.get_date_label();

		parse_data = {
			"national_totals": {
				"confirmed_cases": 0,
				"suspicious_cases": 0,
				"negative_cases":0,
				"deads": 0,
			},
			"states_totals": [],
			"update_label": update_label
			};

		for i in result:
			state_total = {
				"id": i[0],
				"name": i[1],
				"confirmed_cases": int(i[4]),
				"negative_cases": int(i[5]),
				"suspicious_cases": int(i[6]),
				"deads": int(i[7])
			}
			parse_data["states_totals"].append(state_total)
			parse_data["national_totals"]["confirmed_cases"] += state_total["confirmed_cases"]
			parse_data["national_totals"]["suspicious_cases"] += state_total["suspicious_cases"]
			parse_data["national_totals"]["negative_cases"] += state_total["negative_cases"]
			parse_data["national_totals"]["deads"] += state_total["deads"]

		return parse_data

obj = DataToJson()
print(obj.get_stats())