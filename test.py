import ConfigParser


nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    a = '[dummy_section]\n'
    b = f.read()
    config_string = a + b
config = ConfigParser.ConfigParser()
config.read(config_string)
print config_string

#test = config.get('dummy_section', 'rpcuser')
