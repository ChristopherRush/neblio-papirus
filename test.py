import ConfigParser


nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    config_string = '[dummy_section]\n' + f.read()
config = ConfigParser.ConfigParser()
config.read(config_string)

test = config.get('dummy_section', 'rpcuser')

print test
