import ConfigParser

def readToken(config_file, section):
	parser = ConfigParser.ConfigParser()
	parser.read(config_file)
	return parser.get(section, "token")