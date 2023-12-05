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

@app.route("/films")
def films():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = "SELECT * FROM `films` WHERE LOWER(`title`) LIKE LOWER(%s) or LOWER(`director`) LIKE LOWER(%s)"
            search = "%{}%".format(request.args["search"])
            query_args = [search, search]
        else:
            sql = "SELECT * FROM `films`"
        cursor.execute(sql, query_args)
        films = cursor.fetchall()

    return render_template("index.html", films=films, search=request.args.get("search"))


@app.route("/planets")
def planets():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = "SELECT * FROM `planet` WHERE LOWER(`name`) LIKE LOWER(%s) ORDER BY `name` ASC"
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = "SELECT * FROM `planet` ORDER BY `name` ASC"
        cursor.execute(sql, query_args)
        planets = cursor.fetchall()

    return render_template("planets.html", planets=planets, search=request.args.get("search"))


@app.route("/people")
def people():
    with connection.cursor() as cursor:
        query_args = []
        query_extra = ""
        if request.args.get("search"):
            query_extra = """
                WHERE LOWER(`name`) LIKE LOWER(%s)
            """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        sql = """
            SELECT
                `person`.*,
                `eyeColor`.`Color` as ColorOfEyes,
                (select `Name` from planet where `ID`=`HomeWorld`) as `HomeWorldName`,
                (select `Name` from `species` WHERE `ID`=`species`) as `SpecieName`
            FROM `person`
            INNER JOIN `eyeColor` ON `person`.`EyeColor` = `eyeColor`.`ID`
            {}
            ORDER BY `name` ASC
            """.format(query_extra)
        cursor.execute(sql, query_args)
        result = cursor.fetchall()
    return render_template("people.html", people=result, search=request.args.get("search"))


if __name__ == "__main__":
    app.run(debug=config.DEGUB)
