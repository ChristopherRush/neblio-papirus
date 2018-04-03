import ConfigParser
import StringIO

nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    a = '[dummy]\n'
    b = f.read()
    config_string = a + b

buf = StringIO.StringIO(config_string)
config = ConfigParser.ConfigParser()

config.readfp(buf)

print config.get('dummy','rpcuser')



#test = config.get('dummy_section', 'rpcuser')
