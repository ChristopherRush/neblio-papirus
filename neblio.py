from bitcoinrpc.authproxy import AuthServiceProxy
from papirus import Papirus
from papirus import PapirusText
from papirus import PapirusComposite

text = PapirusText()
textNImg = PapirusComposite()
# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://nebliorpc:Dtmqe2aj1Fc35nKMKMrwyCKEYxnatVGpW9tvXhuXdTHt@127.0.0.1:8332")

get_connection = rpc_connection.getinfo()["connections"]
get_balance = rpc_connection.getinfo()["balance"]
get_staking_status = rpc_connection.getstakinginfo()["staking"]

connections = ('Connections: %d' % get_connection)
balance = ('Balance: %d' % get_balance)
staking = ('Staking: %s' % get_staking_status)

textNImg.AddText((connections), 10, 10, Id="Start")

textNImg.AddText((balance), 10, 30, Id="line2" )

textNImg.AddText((staking), 10, 50, Id="line3" )



#print "Connections:", getinfo
print connections
textNImg.WriteAll()
