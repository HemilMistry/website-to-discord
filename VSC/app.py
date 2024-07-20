from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='main/templates', static_url_path='/main/static') #May need editing based on directory

@app.route('/')
def hello():
    return render_template('index.html')

def clearValue():
    with open('main/value.txt', 'w') as clear:
        pass

clearValue()

current_value = None



def flagTrue():
    with open('main/flag.txt', 'w') as editFlag:
        editFlag.write('True')



@app.route('/process', methods=['POST'])
def process():
    flagTrue()
    global current_value
    data = request.get_json()
    current_value = data.get('value', 0)
    result = jsonify({'result': current_value})
    
    with open('main/value.txt', 'w') as f:
        f.write(current_value)

    return result


if __name__ == '__main__':
    app.run(debug=True)
