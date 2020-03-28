# COVID-19 🦠 
Service to get the stats about COVID-19 in Mexico. 

### AWS Lambda
[GET]
`https://dl1ndau7be.execute-api.us-east-1.amazonaws.com/default/coronavirusMexicoStats`

Response
```
{
  "national_totals": {
		"confirmed_cases": 0,
		"suspicious_cases": 0,
		"negative_cases":0,
		"deads": 0,
	},
	"states_totals": [{
			"id": "1",
			"name": "Aguascalientes",
			"confirmed_cases": 0,
			"negative_cases": 0,
			"suspicious_cases": 0,
			"deads": 0
		}],
	"update_label": update_label
}
```

Source: `http://ncov.sinave.gob.mx/mapa.aspx`
