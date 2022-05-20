import cv2
from matplotlib import pyplot as plt



# Image_Read = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# cv2.imshow("image", Image_Read)


# Save Image to disk:-
# image_Read = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# status = cv2.imwrite("New-home.jpg", Image_Read)
# NewReadImg = cv2.imread("New-home.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("New Image", NewReadImg)

# Resize Image:-
# ReadImg = cv2.imread("home.jpg", cv2.IMREAD_GRAYSCALE)
# resized_Image = cv2.resize(ReadImg, (250, 250),
#         interpolation=cv2.INTER_NEAREST)
# cv2.imshow("Resized Image", resized_Image)

#Get Image Shape:-
 # img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
 #
 # print("Height of Image is =====> ", img.shape[0])
 # print("Width of Image is =====> ", img.shape[1])

# Put Text On Image:-

# img = cv2.imread("home.jpg", cv2.IMREAD_GRAYSCALE)
# text_Image = cv2.putText(img, "Amir Ali Anwar", (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 1 , (0, 250, 0), 2)
# #
# cv2.imshow("Text Image", text_Image)

# Draw a Line on an Image:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# line_Image = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
#
# cv2.imshow("Line Image", line_Image)


# Draw a Circle on an Image:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# circle_Image = cv2.circle(img, (500, 300), 40, (0, 250, 0), 3)
#
# cv2.imshow("Circle Image", circle_Image)

# Draw an Reactangle on an Image:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# rectangle_Image = cv2.rectangle(img, (110, 220), (390, 300), (0, 255, 0), 2)
#
# cv2.imshow("Circle Image", rectangle_Image)


# Draw an Square on an Image:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# square_Image = cv2.rectangle(img, (150, 150), (250, 250), (0, 255, 0), 2)
#
# cv2.imshow("square Image", square_Image)

# Convert Image to GrayScale:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("Gray Image", gray_Image)


# Convert GrayScaleImage to RGB:-

# img = cv2.imread("home.jpg", cv2.IMREAD_COLOR)
# gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# rgb_Image = cv2.cvtColor(gray_Image, cv2.COLOR_GRAY2RGB)
#
# cv2.imshow("RGB Image", rgb_Image)
# cv2.imshow("GRAY Image", gray_Image)

# Capture LiveStream From WebCam:-

# cap = cv2.VideoCapture(0)
#
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")
#
# while True:
#     ret, frame = cap.read()
#     frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#     cv2.imshow('Input', frame)
#
#     c = cv2.waitKey(1)
#     if c == 27:
#         break
#
#
# cap.release()
# Read Video From Disk:-

# cap = cv2.VideoCapture('testingvideo.mp4')
# if not cap.isOpened():
#     print("Error opening video file")
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret:
#         resized_Image = cv2.resize(frame, (250, 200),
#                                    interpolation=cv2.INTER_NEAREST)
#         cv2.imshow('Frame', resized_Image)
#     else:
#         break
#
# cap.release()

#Blur an Image:-

# ReadImg = cv2.imread('home.jpg')
# blur_Img = cv2.blur(ReadImg, (10, 10))
# cv2.imshow("Original Image", ReadImg)
# cv2.imshow('blurred image', blur_Img)


# Detect Edges of Object in an Image:

# img = cv2.imread("home.jpg")
# edges = cv2.Canny(img, 100, 200)
#
# cv2.imshow("Original Image", img)
# cv2.imshow("Edge Detection ====> ", edges)

# Detect Contours in an Image:-

# img = cv2.imread("home.jpg")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# edge = cv2.Canny(gray, 100, 200)
#
# counters, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# print("Number of Contours found =====> " + str(len(counters)))


# Crop an Image:-

img = cv2.imread("home.jpg")
cv2.imshow("Original Image", img)

cropped_image = img[0:400, 0:400]

cv2.imshow("cropped", cropped_image)




cv2.waitKey(0)
cv2.destroyAllWindows()
