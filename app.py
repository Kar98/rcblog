import flaskr
print('pre create')
if __name__ == '__main__':
    flaskr.create_app(None).run(debug=False)
print('post create')