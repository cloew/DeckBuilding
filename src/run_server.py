from Server import server

def runserver():
    server.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
	runserver()