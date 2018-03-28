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
get_current_block = rpc_connection.getstakinginfo()["currentblocksize"]
get_difficulty = rpc_connection.getstakinginfo()["difficulty"]

connections = ('Connections: %d' % get_connection)
balance = ('Balance: %d' % get_balance)
staking = ('Staking: %s' % get_staking_status)
currentblock = ('Current Block Size: %d' % get_current_block)
difficulty = ('Difficulty: %d' % get_difficulty)

textNImg.AddText((connections), 10, 10, Id="Start")

textNImg.AddText((balance), 10, 30, Id="line2" )

textNImg.AddText((staking), 10, 50, Id="line3" )

textNImg.AddText((currentblock), 10, 70, Id="line4" )

textNImg.AddText((difficulty), 10, 70, Id="line5" )



#print "Connections:", getinfo
print connections
textNImg.WriteAll()
