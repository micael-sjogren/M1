from waitress import serve
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute_script', methods=['POST'])
def execute_script():
    data = request.json
    print("Received Data:", data)
    script_path = data.get("scriptPath", None)

    if not script_path:
        return jsonify({"message": "Missing scriptPath"}), 400

    command = script_path
 
    try:
        print(f"Executing: {command}")
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        returncode = process.returncode

        if returncode != 0:
            return jsonify({"message": "Error occurred", "stdout": stdout.decode('utf-8'), "stderr": stderr.decode('utf-8')}), 400
        else:
            return jsonify({"message": "Script executed successfully", "stdout": stdout.decode('utf-8'), "stderr": stderr.decode('utf-8')}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
