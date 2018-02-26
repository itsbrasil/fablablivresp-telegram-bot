import ConfigParser

def readConfigData(config_file, section, data):
	parser = ConfigParser.ConfigParser()
	parser.read(config_file)
	return parser.get(section, data)