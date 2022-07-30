from flask import Flask, Response
from flask import request
from main import translateToRoman, translateToUrdu
import json


api = Flask(__name__)
api.config["DEBUG"] = True


# Map the URL ("/translate") to the translate function
@api.route("/translate", methods=["GET"])  # Accept GET requests
def translate():
    # The URL contains three query parameters
    text = request.args.get('text')  # The text to be translated
    from_lang = request.args.get('from_lang')  # The language to translate from
    to_lang = request.args.get('to_lang')  # The language to translate to

    # "ru" represents Roman Urdu and "u" represents Urdu
    if from_lang == "ru" and to_lang == "u":
        data = translateToUrdu(text)
    elif from_lang == "u" and to_lang == "ru":
        data = translateToRoman(text)
    else:
        data = text

    # Convert the translated text to a JSON object
    dict_json = {"data": data}
    data_json = json.dumps(dict_json)

    res = Response(data_json, mimetype="application/json", status=200)
    res.headers.add('Access-Control-Allow-Origin', '*')

    return res


api.run()
