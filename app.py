from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        "id": 1,
        "name": "Nome 01",
        "lang": "python"
    },
    {
        "id": 2,
        "name": "Nome 02",
        "lang": "node"
    },
    {
        "id": 3,
        "name": "Nome 03",
        "lang": "javascript"
    },
    {
        "id": 4,
        "name": "Nome 04",
        "lang": "java"
    },
    {
        "id": 5,
        "name": "Nome 05",
        "lang": "cobol"
    },
    {
        "id": 6,
        "name": "Nome 06",
        "lang": "ruby"
    },
    {
        "id": 7,
        "name": "Nome 07",
        "lang": "react"
    },
    {
        "id": 8,
        "name": "Nome 08",
        "lang": "java"
    },
    {
        "id": 9,
        "name": "Nome 09",
        "lang": "C#"
    },
    {
        "id": 10,
        "name": "Nome 10",
        "lang": "delphi"
    }
]


@app.route("/", methods=["GET"])
def index():
    return "Hello world!!!", 200


@app.route("/devs", methods=["GET"])
def devs_all():
    return jsonify(devs), 200


@app.route("/devs/<string:lang>", methods=["GET"])
def devs_by_lang_get(lang):
    devs_by_lang = [dev for dev in devs if dev["lang"] == lang]
    return jsonify(devs_by_lang), 200


@app.route("/devs/<int:id>", methods=["GET"])
def devs_by_id_get(id):
    devs_by_id = [dev for dev in devs if dev["id"] == id]
    if len(devs_by_id) > 0:
        return jsonify(devs_by_id), 200
    else:
        return jsonify({"error": "not found"}), 404


@app.route("/devs", methods=["POST"])
def devs_save():
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201


@app.route("/devs/<int:id>", methods=["PUT"])
def devs_by_id_put(id):
    devs_by_id = [dev for dev in devs if dev["id"] == id]
    if len(devs_by_id) > 0:
        devs[0]["lang"] = request.get_json().get("lang")

        return jsonify(devs_by_id), 200
    else:
        return jsonify({"error": "not found"}), 404


@app.route("/devs/<int:id>", methods=["DELETE"])
def devs_by_id_delete(id):
    devs_by_id = [dev for dev in devs if dev["id"] == id]
    if len(devs_by_id) > 0:
        devs.remove(devs_by_id)

        return jsonify(devs_by_id), 200
    else:
        return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run()
