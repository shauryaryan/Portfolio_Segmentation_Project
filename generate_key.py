import os
import base64

secret_key = base64.b64encode(os.urandom(24)).decode('utf-8')
print(secret_key)

