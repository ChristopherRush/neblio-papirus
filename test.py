import ConfigParser


nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    config_string = '[dummy_section]\n' + f.read(rpcuser)
config = configparser.ConfigParser()
print config.rpcuser(config_string)
