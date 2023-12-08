import pymysql.cursors

from flask import Flask, render_template, request

import config


connection = pymysql.connect(
    host=config.DATABASE_HOST,
    port=config.DATABASE_PORT,
    user=config.DATABASE_USER,
    password=config.DATABASE_PASSWORD,
    database=config.DATABASE_NAME,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
app = Flask(__name__)


@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello_world_html")
def hello_world_html():
    return render_template("hello.html")


@app.route("/")
def menu():
    return render_template("index.html")

# @app.route("/films")
# def films():
#     with connection.cursor() as cursor:
#         query_args = []
#         if request.args.get("search"):
#             sql = "SELECT * FROM `films` WHERE LOWER(`title`) LIKE LOWER(%s) or LOWER(`director`) LIKE LOWER(%s)"
#             search = "%{}%".format(request.args["search"])
#             query_args = [search, search]
#         else:
#             sql = "SELECT * FROM `films`"
#         cursor.execute(sql, query_args)
#         films = cursor.fetchall()
#
#     return render_template("index.html", films=films, search=request.args.get("search"))
#
#
# @app.route("/planets")
# def planets():
#     with connection.cursor() as cursor:
#         query_args = []
#         if request.args.get("search"):
#             sql = "SELECT * FROM `planet` WHERE LOWER(`name`) LIKE LOWER(%s) ORDER BY `name` ASC"
#             search = "%{}%".format(request.args["search"])
#             query_args = [search]
#         else:
#             sql = "SELECT * FROM `planet` ORDER BY `name` ASC"
#         cursor.execute(sql, query_args)
#         planets = cursor.fetchall()
#
#     return render_template("planets.html", planets=planets, search=request.args.get("search"))
#
#
# @app.route("/people")
# def people():
#     with connection.cursor() as cursor:
#         query_args = []
#         query_extra = ""
#         if request.args.get("search"):
#             query_extra = """
#                 WHERE LOWER(`name`) LIKE LOWER(%s)
#             """
#             search = "%{}%".format(request.args["search"])
#             query_args = [search]
#         sql = """
#             SELECT
#                 `person`.*,
#                 `eyeColor`.`Color` as ColorOfEyes,
#                 (select `Name` from planet where `ID`=`HomeWorld`) as `HomeWorldName`,
#                 (select `Name` from `species` WHERE `ID`=`species`) as `SpecieName`
#             FROM `person`
#             INNER JOIN `eyeColor` ON `person`.`EyeColor` = `eyeColor`.`ID`
#             {}
#             ORDER BY `name` ASC
#             """.format(query_extra)
#         cursor.execute(sql, query_args)
#         result = cursor.fetchall()
#     return render_template("people.html", people=result, search=request.args.get("search"))

@app.route("/drogas")
def drogas():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = f"""
                WHERE LOWER(B.bairro_nome) LIKE LOWER({request.args["search"]})
            """
            search = "%{}%".format()
            query_args = [search]
        sql = """
WITH DrogaRanking AS (
    SELECT
        B.nome_bairro,
        D.tipo_droga,
        COUNT(*) AS quantidade_utilizacao,
        ROW_NUMBER() OVER (PARTITION BY B.nome_bairro ORDER BY COUNT(*) DESC) AS ranking
    FROM
        Pessoa AS P
        INNER JOIN faz_uso AS F ON P.ID = F.ID
        INNER JOIN Drogas AS D ON D.codigo = F.codigo
        INNER JOIN coleta AS C ON C.ID = P.ID
        INNER JOIN bairro AS B ON B.Codigo_da_RA = C.Codigo_da_RA
    GROUP BY
        B.nome_bairro, D.tipo_droga
)
SELECT
    nome_bairro,
    tipo_droga,
    quantidade_utilizacao
FROM
    DrogaRanking
WHERE
    ranking < 4;
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("drogas.html", drogas=result, search=request.args.get("search"))

@app.route("/localizacoes")
def localizacoes():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = f"""
                WHERE LOWER(b.nome_bairro) LIKE LOWER(%s)
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
            query_args = [f"%{request.args['search']}%"]
        sql = """
            SELECT
                b.nome_bairro,
                (
                    SELECT COUNT(DISTINCT p.ID)
                    FROM Pessoa p
                    JOIN vive v ON p.ID = v.ID
                    JOIN realizou_se r ON v.ID = r.ID
                    JOIN coleta c ON r.ID = c.ID
                    WHERE b.Codigo_da_RA = c.Codigo_da_RA
                ) AS Quantidade_Pessoas
            FROM
                bairro b
            ORDER BY Quantidade_Pessoas DESC;
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("localizacoes.html", localizacoes=result, search=request.args.get("search"))

@app.route("/motivos")
def motivos():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = f"""
                WHERE LOWER(b.nome_bairro) LIKE LOWER(%s)
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
            query_args = [f"%{request.args['search']}%"]
        sql = """
            SELECT
                B.nome_bairro,
                SR.Motivo_dormir_rua,
                COUNT(*) AS numero_ocorrencias
            FROM
                vive AS V JOIN
                SituacaoRua AS SR ON V.ID = SR.ID
            JOIN
                coleta as C ON
                C.ID = V.ID
            JOIN
                bairro as B ON
                B.Codigo_da_Ra = C.Codigo_da_Ra
            GROUP BY
                B.nome_bairro,
                SR.Motivo_dormir_rua
            ORDER BY
                B.nome_bairro ASC,
                numero_ocorrencias DESC;
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("motivos.html", motivos=result, search=request.args.get("search"))

@app.route("/doencas")
def doencas():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = f"""
                WHERE LOWER(b.nome_bairro) LIKE LOWER(%s)
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
            query_args = [f"%{request.args['search']}%"]
        sql = """
WITH CondicaoRanking AS (
    SELECT
        b.nome_bairro,
        s.condicao,
        COUNT(*) AS quantidade_repeticoes,
        ROW_NUMBER() OVER (PARTITION BY b.nome_bairro ORDER BY COUNT(*) DESC) AS ranking
    FROM
        bairro b
        JOIN coleta c ON b.Codigo_da_RA = c.Codigo_da_RA
        JOIN realizou_se r ON c.ID = r.ID AND b.Codigo_da_RA = r.Codigo_da_RA
        JOIN vive v ON r.ID = v.ID
        JOIN estado_de e ON v.ID = e.ID
        JOIN Saude s ON e.codigo = s.codigo
    GROUP BY
        b.nome_bairro, s.condicao
)
SELECT
    nome_bairro,
    condicao,
    quantidade_repeticoes
FROM
    CondicaoRanking
WHERE
    ranking <= 2;
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("doencas.html", doencas=result, search=request.args.get("search"))

@app.route("/documentos")
def documentos():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = f"""
                WHERE LOWER(b.nome_bairro) LIKE LOWER(%s)
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
            query_args = [f"%{request.args['search']}%"]
        sql = """
SELECT
    tipo_documento,
    COUNT(*) AS contagem_documentos_por_tipo
FROM (
    SELECT
        P.ID AS idPessoa,
        D.tipo_documento
    FROM Pessoa AS P
    JOIN possui AS PO ON P.ID = PO.morador_id
    JOIN Documentos AS D ON PO.codigo = D.codigo
    GROUP BY P.ID, D.tipo_documento
) AS subconsulta
GROUP BY tipo_documento;
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("documentos.html", documentos=result, search=request.args.get("search"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=config.DEGUB)
