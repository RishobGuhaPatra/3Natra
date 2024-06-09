import fireworks.client
import base64

# Helper function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# The path to your image
image_path = "captured_image.jpg"

# The base64 string of the image
image_base64 = encode_image(image_path)

fireworks.client.api_key = "ZjmbkO29n0auyzepBuagyAWfHgGs9qEwx3czl8Wuxx1TlIKI"

response = fireworks.client.ChatCompletion.create(
  model = "accounts/fireworks/models/firellava-13b",
  messages = [{
    "role": "user",
    "content": [{
      "type": "text",
#      "text": "Can you describe this image?",
#       "text": "please describe the image?",
        "text": "text",
    }, {
      "type": "image_url",
      "image_url": {
           "url": f"data:image/jpeg;base64,{image_base64}"
#          "url": "https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
      },
    }, ],
  }],
)
print(response.choices[0].message.content)
