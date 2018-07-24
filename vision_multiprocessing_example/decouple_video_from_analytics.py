import multiprocessing
import cv2
import time

def detect_faces(records, name):

	face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')

	while True:

		if len(records)  > 0:
			
			frame = records[-1]
			# convert to gray scale of each frames
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# Detects faces of different sizes in the input image
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)

			for (x,y,w,h) in faces:
			    # To draw a rectangle in a face 
			    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 
			    roi_gray = gray[y:y+h, x:x+w]
			    roi_color = frame[y:y+h, x:x+w]

			    # Detects eyes of different sizes in the input image
			    # eyes = eye_cascade.detectMultiScale(roi_gray) 

			    #To draw a rectangle in eyes
			    # for (ex,ey,ew,eh) in eyes:
			        # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

			# Display an image in a window
			cv2.imshow(name, frame)


			k = cv2.waitKey(1)
			if k == 27:
				cv2.destroyAllWindows()
				break
			
		else:
			print("No images present")
			cv2.destroyAllWindows()



def detect_eyes(records, name):

	face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./models/haarcascade_eye.xml')

	while True:
		
		if len(records)  > 0:
			
			frame = records[-1]
			# convert to gray scale of each frames
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# Detects faces of different sizes in the input image
			faces = face_cascade.detectMultiScale(gray, 1.3, 5)

			for (x,y,w,h) in faces:
			    # To draw a rectangle in a face 
			    # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 
			    roi_gray = gray[y:y+h, x:x+w]
			    roi_color = frame[y:y+h, x:x+w]

			    # Detects eyes of different sizes in the input image
			    eyes = eye_cascade.detectMultiScale(roi_gray) 

			    #To draw a rectangle in eyes
			    for (ex,ey,ew,eh) in eyes:
			        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

			# Display an image in a window
			cv2.imshow(name, frame)


			k = cv2.waitKey(1)
			if k == 27:
				cv2.destroyAllWindows()
				break
			
		else:
			print("No images present")
			cv2.destroyAllWindows()



def print_records(records):

	while True:
		time.sleep(2)
		if len(records)  > 0:
			frame = records[-1]
			cv2.imshow("inside_print_record", frame)

			k = cv2.waitKey(10)
			if k == 27:
				cv2.destroyAllWindows()
				break
			
		else:
			print("No images present")
			cv2.destroyAllWindows()


 
def insert_record(records):
	
	video_path = '/media/anuj/Work-HDD/WORK/CLOUD-DRIVE/Google-Drive/Computer-Vision/Sample-Videos/RTSP-supported-videos/obama.webm'
	cap = cv2.VideoCapture(video_path)

	while True:
		# time.sleep(2)
		ret, frame = cap.read()
		records.append(frame.copy())
		
		if len(records) > 150:
			records.pop(0)
		cv2.imshow("inside_insert_record", frame)
		k = cv2.waitKey(1)
		if k == 27:
			break
			cap.release()
			cv2.destroyAllWindows()

	cap.release()
	cv2.destroyAllWindows()

 
if __name__ == '__main__':
	with multiprocessing.Manager() as manager:
		# creating a list in server process memory
		records = manager.list([])
		
		# creating new processes
		p1 = multiprocessing.Process(target=insert_record, args=(records,))
		p1.start()
		
		p2 = multiprocessing.Process(target=detect_faces, args=(records, "face-1"))
 		p2.start()

 		p3 = multiprocessing.Process(target=detect_eyes, args=(records, "eyes-1"))
 		p3.start()

 		p4 = multiprocessing.Process(target=detect_eyes, args=(records, "eyes-2"))
 		p4.start()

		p1.join()
		p2.join()
		p3.join()
		p4.join()
