from flask import Flask, jsonify
import boto3
from dotenv import load_dotenv
from boto3.dynamodb.conditions import Key
# Load environment variables from .env
load_dotenv()

app = Flask(__name__)


@app.route('/secret', methods=['GET'])
def get_secret():
    code_name = 'thedoctor'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('devops-challenge')
    try:
        response = table.query(
            KeyConditionExpression=Key(
                'code_name').eq(code_name)
        )
        item = response.get('Item')
        if not item or 'secret_code' not in item:
            return jsonify({'error': 'Secret code not found'}), 404
        return jsonify({'secret_code': {item['secret_code']}})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'container': 'https://hub.docker.com/repository/docker/flaymister/thedoctor-docker/general',
        'project': 'https://github.com/flaymaster/the_doctor#'
    })


if __name__ == '__main__':
    app.run(debug=True)
