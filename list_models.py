from google.generativeai import Client

client = Client()  # Make sure GOOGLE_APPLICATION_CREDENTIALS is set
models = client.list_models()

for m in models.models:
    print("Model:", m.name)
    print("Supported methods:", m.supported_methods)
    print("---")
