from datetime import datetime

from features.recognition.FaceDetection import FaceDetection
from features.streaming.CameraStream import CameraStream
from models.staff import Staff
from models.visitor import Visitor
from persistence.mongo import MongoConnectorService
from persistence.crud import CRUD


class Bootstrapper:
    @staticmethod
    def bootstrap():
        # TODO: Avoid hard coding use standard preference techniques
        data_source = MongoConnectorService(('intruder', 'Kutte@P00nch'), 'visitor')
        db = CRUD(data_source)
        # Store the visitor or staff name
        visitor = Visitor(1234, 'sample_visitor', [], datetime.now(), '123445', None, None)
        db.store_data(visitor)
        print('Visitor Added')
        # update the visitor/staff exit time
        visitor.exit_timestamp = datetime.now()
        print('Visitor exit timestamp updated')
        # Start the Camera Stream
        stream = CameraStream.get_instance(None, None)
        print('Camera Stream Started')
        # Pass the stream to face detection
        face_detector = FaceDetection()
        print('Face Detector initiated')
        frame = stream.get_current_frame()
        print('Read current frame')
        while frame is not None:
            # get the extracted faces
            # pass the extracted face for face recognition in the current frame
            # if face found check the exit time
            # notify for intrusion if there is any
            print('Read current Frame')
            frame = stream.get_current_frame()
        # make the process multi threaded
