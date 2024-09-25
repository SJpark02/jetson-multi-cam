import cv2

def gstreamer_pipeline(port):
    return f'udpsrc port={port} ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink'

# 각 Jetson 장치에서 스트리밍하는 포트를 설정합니다.
ports = [5000, 5001, 5002, 5003, 5004]
streams = [cv2.VideoCapture(gstreamer_pipeline(port), cv2.CAP_GSTREAMER) for port in ports]

while True:
    for i, stream in enumerate(streams):
        ret, frame = stream.read()
        if ret:
            cv2.imshow(f'Camera {i}', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

for stream in streams:
    stream.release()

cv2.destroyAllWindows()
