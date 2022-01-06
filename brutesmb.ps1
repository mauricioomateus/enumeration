for /f "tokens=1,2" %i in (lista) do net use \172.16.1.4 %j /u:%i
