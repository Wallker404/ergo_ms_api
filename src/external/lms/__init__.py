import configparser

config = configparser.ConfigParser()

MODULE_PATH = 'src/external/lms/'
CONF_PATH = MODULE_PATH + '.conf'

config.read(CONF_PATH)