import configparser

def readConfigData(config_file, section, data):
	parser = configparser.ConfigParser()
	parser.read(config_file)
	return parser.get(section, data)