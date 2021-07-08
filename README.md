# MariaDb-Python

# 1. Visão geral

MariaDB fornece suporte Python por meio do Conector/Python MariaDB, que está disponível por meio do Python Package Index. Para instalar, use o PIP:

```
$ pip3 install mariadb
```

# 2. Conectando ao Servidor MariaDB

> 2.1. Para se conectar ao Servidor MariaDB usando MariaDB Connector/Python, você deve importá-lo primeiro, assim como faria com qualquer outro módulo: import mariadb

> 2.2. Em seguida, estabeleça uma conexão de banco de dados com a função connect(). A função leva uma série de argumentos nomeados especificando suas credenciais de cliente, como nome de usuário, host, senha. Se você estiver usando uma instância de banco de dados no SkySQL, essas informações são fornecidas na página Detalhes do serviço para sua instância de banco de dados.

A conexão fornece uma interface para configurar a conexão do seu aplicativo com o servidor MariaDB.

> 2.3 Por último, chame o método cursor() na conexão para recuperar o cursor.

O cursor fornece uma interface para interagir com o servidor, como executar consultas SQL e gerenciar transações.
