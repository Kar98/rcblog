from flaskr import create_app

if __name__ == '__main__':
    print('in if')
    create_app = create_app()
    create_app.run()
else:
    print('in else')
    app = create_app()
