import ConfigParser


nebliopath='/home/pi/.neblio/neblio.conf'


with open('/home/pi/.neblio/neblio.conf', 'r') as f:
    config_string = "[dummy_section]\n" + f.read()
config = ConfigParser.ConfigParser()
config.read(config_string)

test = config.get('dummy_section', 'rpcuser')

print test
