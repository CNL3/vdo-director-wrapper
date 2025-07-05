
from flask import Flask, request, render_template_string
import datetime
import random
import string

app = Flask(__name__)

def generate_room_name():
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"room{now}_{suffix}"

def generate_push_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route("/vdo-director")
def serve_dynamic_vdo_wrapper():
    room_name = generate_room_name()
    push_token = generate_push_token()

    obs_camera_name = "OBS Virtual Camera"  # Replace with your actual virtual camera name

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Auto VDO.Ninja Director Join</title>
        <style>
            body {{
                background-color: rgba(0, 0, 0, 0);
                margin: 0;
                overflow: hidden;
            }}
            video {{
                height: 100vh !important;
                width: auto !important;
                object-fit: contain;
            }}
        </style>
    </head>
    <body>
        <script>
            const room = "{room_name}";
            const push = "{push_token}";
            const cam = encodeURIComponent("{obs_camera_name}");
            const url = `https://vdo.ninja/?room=${{room}}&push=${{push}}&vd=${{cam}}&autostart&aspect=9:16&director`;
            window.location.href = url;
        </script>
    </body>
    </html>
    """

    return render_template_string(html_template)
