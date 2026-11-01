from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/api/hello")
def hello():
    return jsonify(
        {
            "message": "Hello from Python Flask!",
            "service": "flask-backend",
            "version": "1.0.0",
        }
    )


@app.get("/api/products")
def products():
    return jsonify(
        {
            "products": [
                {"id": 1, "name": "Laptop", "price": 50000},
                {"id": 2, "name": "Keyboard", "price": 2000},
                {"id": 3, "name": "Mouse", "price": 800},
            ]
        }
    )


@app.get("/healthz")
def health():
    return jsonify({"status": "healthy"}), 200


@app.get("/readyz")
def readiness():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
