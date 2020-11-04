from flask import Flask
from flask import Response, request
from flask import jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    return 'hello_world!'

    res = {
    'result_code': '0000',
    'result_value': name
    }
    jsonRtn = jsonify(res)

    return jsonRtn


@app.route('/copy', methods=['POST'])
def doCopyFile():
    document_path = request.json['document_path']
    document_path2 = request.json['document_path2']



    os.system('cp ' + document_path + ' ' + document_path2)

    res = {
    'result_code': '0000',
    'result_value': ""
    }

    jsonRtn = jsonify(res)


    print(document_path +  ' ' + document_path2)

    return jsonRtn


@app.route('/move', methods=['POST'])
def doMoveFile():
    try:
        document_path = request.json['document_path']
        document_path2 = request.json['document_path2']

        document_path2 = document_path2
        os.system('mv ' + document_path + ' ' + document_path2)

        res = {
            'result_code': '0000',
            'result_value': '정상적으로 move 되었습니다'
        }
        jsonRtn = jsonify(res)



    except Exception as msg:

        res = {
            'result_code': '0000',
            'result_value': str(msg)
        }
        jsonRtn = jsonify(res)

    return jsonRtn



@app.route('/del', methods=['POST'])
def doDelFile():
    document_path = request.json['document_path']

    os.system('rm -rf ' + document_path)

    res = {
    'result_code': '0000',
    'result_value': '삭제완료'
    }
    jsonRtn = jsonify(res)

    return jsonRtn

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8011)

