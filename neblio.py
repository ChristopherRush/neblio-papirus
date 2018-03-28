from bitcoinrpc.authproxy import AuthServiceProxy
from papirus import Papirus
from papirus import PapirusText
from papirus import PapirusComposite

text = PapirusText()
textNImg = PapirusComposite()
# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://nebliorpc:Dtmqe2aj1Fc35nKMKMrwyCKEYxnatVGpW9tvXhuXdTHt@127.0.0.1:8332")
getinfo = rpc_connection.getinfo()["connections"]


connections = ('Connections: %d' % getinfo)
textNImg.AddText((connections), 10, 10, Id="Start")

textNImg.AddText("hello world", 10, 20, Id="line2" )



#print "Connections:", getinfo
print connections
textNImg.WriteAll()
