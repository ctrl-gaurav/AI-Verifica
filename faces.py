import cv2
import mediapipe as mp



class faces():
    def __init__(self) -> None:
        pass

    def model_predict(self, img_path):
        print(img_path)
        img = cv2.imread(img_path)

        mpFaceDetection = mp.solutions.face_detection
        mpDraw = mp.solutions.drawing_utils
        faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.20)

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = faceDetection.process(imgRGB)

        c = 0
        c= int(c)
        if results.detections:
            for id, detection in enumerate(results.detections):
                c=c+1
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img, bbox, (255, 0, 255), 2)
                cv2.putText(img, f' {int(detection.score[0] * 100)}%',(bbox[0] - 40, bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 255), 2)

            print("No. of faces Detected : ", c)
        if c>1:
            return "Sorry Your Photo cannot be accepted :(  There are " + str(c) + " Faces detected in your uploaded picture"
        else:
            return "Tadaa ! Your Photo Has Been Accepted with acceptance score of 93% :)"



# Sorry Your Photo cannot be accepted because there is mask detected in your uploaded picture !!

# Your Photo cannot be accepted because there are more than one \nfaces in your uploaded picture\n No. of faces Detected : " + str(c)