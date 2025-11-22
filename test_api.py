import requests

url = "http://localhost:3000/process/image"

# Create a dummy image
from PIL import Image
import io

img = Image.new('RGB', (100, 100), color = 'red')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

files = {
    'image': ('test.png', img_byte_arr, 'image/png'),
    'width': (None, '50'),
    'height': (None, '50'),
    'format': (None, 'jpeg')
}

try:
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print("Success! Image processed.")
        with open("output.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Connection failed: {e}")
