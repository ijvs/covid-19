import requests
import json 
import re

def get_date_label():
	url = "http://ncov.sinave.gob.mx/mapa.aspx"
	req = requests.get(url)
	try:
		return re.findall(r'(Cierre con corte.+?)";',req.text)[-1]
	except Exception as e:
		return ""

def get_stats(resource):
	url = "http://ncov.sinave.gob.mx/Mapa45.aspx/Grafica"+resource
	req = requests.post(url, data={}, headers= {"Content-Type":"application/json; charset=utf-8"})

	raw_data = json.loads(req.text)["d"]
	result = json.loads(raw_data)
	update_label = get_date_label();

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

last_resource = "23"
print(get_stats(last_resource))
	























