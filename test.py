import ConfigParser
import StringIO

nebliopath='/home/pi/.neblio/neblio.conf'


with open(nebliopath, 'r') as f:
    a = '[dummy_section]\n'
    b = f.read()
    config_string = a + b
config = ConfigParser.ConfigParser()

buf = StringIO.StringIO(config_string)
print config.readfp(buf)



#test = config.get('dummy_section', 'rpcuser')
