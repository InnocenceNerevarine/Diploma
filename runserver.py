from waitress import serve
import os
from ProvodkaShop.wsgi import application

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    serve(application, host='localhost', port=port)