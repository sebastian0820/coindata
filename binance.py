import websocket
import json

# Binance WebSocket endpoint for real-time data of a specific symbol (e.g., BTC/USDT)
socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

def on_message(ws, message):
    json_message = json.loads(message)
    price = float(json_message['p'])
    print(f"BTC/USDT: ${price:.2f}")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    print("WebSocket connection opened")

# Create a WebSocket app
ws = websocket.WebSocketApp(socket,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open

# Run the WebSocket app
ws.run_forever()