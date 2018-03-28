from bitcoinrpc.authproxy import AuthServiceProxy
from papirus import Papirus
from papirus import PapirusText


rot = 0, 90, 180 or 270
text = PapirusText([rotation = rot])

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://nebliorpc:Dtmqe2aj1Fc35nKMKMrwyCKEYxnatVGpW9tvXhuXdTHt@127.0.0.1:8332")
getinfo = rpc_connection.getinfo()["connections"]

text.write("Connections:", getinfo)
print "Connections:", getinfo
