import ConfigParser


nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    config_string = '[dummy_section]\n' + f.read()
config = ConfigParser.ConfigParser()
config.read_string(config_string)

print config.get('dummy_section', 'rpcuser')
