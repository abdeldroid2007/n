import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def process_post_request():
    d = request.json
    uuid = d.get['uuid']
    id = d.get['id']
    prompt = d.get['prompt']
    
    result = process_values(uuid, id, prompt)
    
    return result



# async function send(prompt, uuid, id) {
def send(prompt, uuid, id):
    txt = prompt
    uuid = uuid
    messageId = id

    def getdata():
        return {
            'messages': [{
                'id': messageId,
                'content': txt,
                'role': 'system'
            }],
            'id': id,
            'previewToken': None,
            'userId': uuid,
            'codeModelMode': True,
            'agentMode': [],
            'trendingAgentMode': [],
            'isMicMode': False,
            'isChromeExt': False,
            'githubToken': None,
            'webSearchMode': False,
            'maxTokens': "10240"
        }

    url = 'https://www.blackbox.ai/api/chat'

    try:
        response = requests.post(url, json=getdata())
        response.raise_for_status()

        result = response.json()
        return result
        # Process the 'result' here. This is where you would handle
        # the response from the blackbox.ai API.

    except requests.exceptions.HTTPError as err:
        print(f'HTTP error! status: {err}')
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    app.run()
