
Você precisa ter o mysql instalado e executando.

Eu recomendo [criar uma virtual-env em python](https://docs.python.org/pt-br/3/library/venv.html) para installar o projeto

Após isso mude as configurações do arquivo `config.yaml` com as configurações do seu banco.
OBS: Se você estiver usando um `host`ou uma porta diferente do padrão, apenas adicione junto com os outros campos um campo `host: "meu_novo_host"`e `port: XXXX`substituindo os valores pelos seus.

Você precisará restaurar o bancos de dados, para isso:
```sh
$ mysql -u root -u
mysql > CREATE DATABASE popRua;
mysql > exit;

$ mysql -u root -u popRua < popRua.sql;

$ python3 setup.py
```

Após essas etapas, você pode rodar o projeto com :
```sh
$ python3 app.py
```

---

Projeto baseado no do João, sobre [Star Wars](https://gitlab.com/joaofreires/bd1-desenvolviment-web).
