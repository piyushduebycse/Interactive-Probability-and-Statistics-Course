import sys
sys.path.append('/opt/.manus/.sandbox-runtime')
from data_api import ApiClient
import json

client = ApiClient()

# Search for economic indicators that could be useful for statistics examples
# Using string for pageSize to avoid the error
indicators = client.call_api('DataBank/indicator_list', query={'q': 'GDP', 'pageSize': '10'})

# Save the results to a JSON file
with open('gdp_indicators.json', 'w') as f:
    json.dump(indicators, f, indent=4)

print("GDP indicators saved to gdp_indicators.json")

# Search for population indicators
population_indicators = client.call_api('DataBank/indicator_list', query={'q': 'population', 'pageSize': '10'})

# Save the results to a JSON file
with open('population_indicators.json', 'w') as f:
    json.dump(population_indicators, f, indent=4)

print("Population indicators saved to population_indicators.json")

# Search for education indicators
education_indicators = client.call_api('DataBank/indicator_list', query={'q': 'education', 'pageSize': '10'})

# Save the results to a JSON file
with open('education_indicators.json', 'w') as f:
    json.dump(education_indicators, f, indent=4)

print("Education indicators saved to education_indicators.json")

# Search for health indicators
health_indicators = client.call_api('DataBank/indicator_list', query={'q': 'health', 'pageSize': '10'})

# Save the results to a JSON file
with open('health_indicators.json', 'w') as f:
    json.dump(health_indicators, f, indent=4)

print("Health indicators saved to health_indicators.json")
