from picamera import PiCamera
from time import sleep

class Camera:
    
    cam = None

    def getSensor():
        camera = PiCamera()

        if camera == None:
            print("Pi Camera is Not Connected", \
                file=sys.stderr)
            sys.exit(0)
            return
        
        Camera.cam = camera
        print("Camera Is Connected")
        return camera
    
    def stopRecording():
        Camera.cam.stop_recording()
    
    def startRecording():
        Camera.cam.start_recording("log/video.h264")