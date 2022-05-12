import csv,datetime,json,pytz,xml.etree.ElementTree as ET

def update_jmeter_log(file_name):
	log_file = open(file_name)
	csvreader = csv.reader(log_file)
	header = next(csvreader)
	for row in csvreader:
		if(not row[3]=='200'):
			if(row[8]==''): 
				row[8]='N/A'

			utc_datetime = datetime.datetime.utcfromtimestamp(float(row[0]) / 1000.)
			row[0] = utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('America/Los_Angeles')).strftime('%Y-%m-%d %H:%M:%S %Z')
			print(row[0],row[2],row[3],row[4],row[8],sep=', ')
	log_file.close()

update_jmeter_log("Jmeter_log1.jtl")
update_jmeter_log("Jmeter_log2.jtl")


def csv_update_file(x,y):
	element_tree = ET.parse('test_payload1.xml')
	root_element = element_tree.getroot()
	root_element[0][2][0].text=(datetime.datetime.now() + datetime.timedelta(days=x)).strftime('%Y%m%d')
	root_element[0][2][1].text=(datetime.datetime.now() + datetime.timedelta(days=y)).strftime('%Y%m%d')
	result_xml = ET.tostring(root)
	with open("test_payload2.xml", "wb") as f:
    		f.write(result_xml)

csv_update_file(11,22)


def json_delete_attribute(x): 
	json_file = open('test_payload.json')
	json_data = json.load(json_file)
	if x in json_data:
		del json_data[x]
	if(x in json_data['inParams']):
		del json_data['inParams'][x]
	with open("test_payload2.json", "w") as outfile:
    		json.dump(json_data, outfile)
	json_file.close()

json_delete_attribute('appdate')
