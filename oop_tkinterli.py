import cv2
import numpy as np
import imutils
from abc import ABC, abstractmethod
from tkinter import *
import tkinter
from PIL import Image,ImageTk

class tennisBallDetect(ABC):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.lower = {'green': (66, 122, 129), 'yellow': (23, 59, 119)}
        self.upper = {'green': (86, 255, 255), 'yellow': (54, 255, 255)}

        self.colors = {'red': (0, 0, 255), 'green': (0, 255, 0), 'blue': (255, 0, 0), 'yellow': (0, 255, 217),
                       'orange': (0, 140, 255)}

    @abstractmethod
    def number_of_balls(self):
        pass

    @abstractmethod
    def balls_coordinates(self):
        pass


class regionNumber(tennisBallDetect):

    def region_number(self):
        x1 = 0
        y1 = 0
        x2 = 120
        y2 = 600

        for j in range(5):
            self.r = cv2.rectangle(self.frame, (x1, y1), (x2, y2), (100, 50, 200), 2)
            x1 += 120
            x2 += 120

            if len(self._cnts) == 1:
                for i in range(0, 1):
                    if self.radius > 0.5 and self.radius < 55:
                        if str(self._centers[i]) < str((240, 600)) and str(self._centers[i]) > str((120, 600)):
                            cv2.putText(self.frame, "2.Region:1 ball" + str(self._centers[0]), (120, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        elif str(self._centers[i]) < str((360, 600)) and str(self._centers[i]) > str((240, 600)):
                            cv2.putText(self.frame, "3.Region:1 ball" + str(self._centers[0]), (240, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((480, 600)) and str(self._centers[i]) > str((360, 600)):
                            cv2.putText(self.frame, "4.Region:1 ball" + str(self._centers[0]), (360, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((600, 600)) and str(self._centers[i]) > str((480, 600)):
                            cv2.putText(self.frame, "5.Region:1 ball" + str(self._centers[0]), (480, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        else:
                            cv2.putText(self.frame, "1.Region:1 ball" + str(self._centers[0]), (10, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                    elif self.radius > 55 and self.radius < 101:
                        if str(self._centers[i]) < str((240, 600)) and str(self._centers[i]) > str((120, 600)):
                            cv2.putText(self.frame, "2.Region:2 ball" + str(self._centers[0]), (120, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        elif str(self._centers[i]) < str((360, 600)) and str(self._centers[i]) > str((240, 600)):
                            cv2.putText(self.frame, "3.Region:2 ball" + str(self._centers[0]), (240,55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((480, 600)) and str(self._centers[i]) > str((360, 600)):
                            cv2.putText(self.frame, "4.Region:2 ball" + str(self._centers[0]), (360, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((600, 600)) and str(self._centers[i]) > str((480, 600)):
                            cv2.putText(self.frame, "5.Region:2 ball" + str(self._centers[0]), (480, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        else:
                            cv2.putText(self.frame, "1.Region:1 ball" + str(self._centers[0]), (10, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)



                    i += 1

            elif len(self._cnts) == 2 and self.radius < 55:
                for i in range(0, 1):
                    if str(self._centers[i]) < str((120, 600)):
                        print("1")
                    elif str(self._centers[i]) < str((240, 600)) and str(self._centers[i]) > str((120, 600) and self._centers[i+1]) < str((240, 600)) and str(self._centers[i+1]) > str((120, 600)):
                        cv2.putText(self.frame, "2.Region:first ball" + str(self._centers[i]), (120, 65),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(self.frame, "2.Region:2. ball" + str(self._centers[i+1]), (120, 75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                    elif str(self._centers[i]) < str((360, 600)) and str(self._centers[i]) > str((240, 600) and self._centers[i+1]) < str((360, 600)) and str(self._centers[i+1]) > str((240, 600) ):
                        cv2.putText(self.frame, "3.Region:first ball" + str(self._centers[i]), (240, 65),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(self.frame, "3.Region:2. ball" + str(self._centers[i + 1]), (240, 75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                    elif str(self._centers[i]) < str((480, 600)) and str(self._centers[i]) > str((360, 600) and self._centers[i+1]) < str((480, 600)) and str(self._centers[i+1]) > str((360, 600) ):
                        cv2.putText(self.frame, "4.Region:first ball" + str(self._centers[i]), (360, 65),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(self.frame, "4.Region:2. ball" + str(self._centers[i + 1]), (360, 75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                    elif str(self._centers[i]) < str((600, 600)) and str(self._centers[i]) > str((480, 600) and self._centers[i+1]) < str((600, 600)) and str(self._centers[i+1]) > str((480, 600)  ):
                        cv2.putText(self.frame, "5.Region:first ball" + str(self._centers[i]), (480, 65),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)
                        cv2.putText(self.frame, "5.Region:2. ball" + str(self._centers[i + 1]), (480, 75),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 0, 255), 2)

                    else :
                        if str(self._centers[i]) < str((240, 600)) and str(self._centers[i]) > str((120, 600)):
                            cv2.putText(self.frame, "2.Region:1 ball" + str(self._centers[0]), (120, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        elif str(self._centers[i]) < str((360, 600)) and str(self._centers[i]) > str((240, 600)):
                            cv2.putText(self.frame, "3.Region:1 ball" + str(self._centers[0]), (240, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((480, 600)) and str(self._centers[i]) > str((360, 600)):
                            cv2.putText(self.frame, "4.Region:1 ball" + str(self._centers[0]), (360, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i]) < str((600, 600)) and str(self._centers[i]) > str((480, 600)):
                            cv2.putText(self.frame, "5.Region:1 ball" + str(self._centers[0]), (480, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        else:
                            cv2.putText(self.frame, "1.Region:1 ball" + str(self._centers[0]), (10, 55),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)



                        if str(self._centers[i + 1]) < str((240, 600)) and str(self._centers[i + 1]) > str(
                                (120, 600)):
                            cv2.putText(self.frame, "2.Region:2.ball" + str(self._centers[1]), (120, 85),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        elif str(self._centers[i + 1]) < str((360, 600)) and str(self._centers[i + 1]) > str(
                                (240, 600)):
                            cv2.putText(self.frame, "3.Region:2. ball" + str(self._centers[1]), (240, 85),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i + 1]) < str((480, 600)) and str(self._centers[i + 1]) > str(
                                (360, 600)):
                            cv2.putText(self.frame, "4.Region:2.ball" + str(self._centers[1]), (360, 85),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)
                        elif str(self._centers[i + 1]) < str((600, 600)) and str(self._centers[i + 1]) > str(
                                (480, 600)):
                            cv2.putText(self.frame, "5.Region:2.ball" + str(self._centers[1]), (480, 85),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                        else:
                            cv2.putText(self.frame, "1.Region:2.ball" + str(self._centers[i]), (10, 85),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                        (0, 0, 255), 2)

                    i += 1
            #elif len(self._cnts) == 3:

    def number_of_balls(self):

        while self.cap.isOpened():
            _, self.frame = self.cap.read()
            self.frame = imutils.resize(self.frame, width=600)
            self.blurred = cv2.GaussianBlur(self.frame, (11, 11), 0)
            self.hsv = cv2.cvtColor(self.blurred, cv2.COLOR_BGR2HSV)

            regionNumber.balls_coordinates(self)  ############################

            if len(self._cnts) == 1:
                if self.radius > 0.5 and self.radius < 55:
                    cv2.putText(self.frame,"Number Of Balls:"+"1",(0,15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (34,248,224), 2)
                    regionNumber.region_number(self)


                elif self.radius > 55 and self.radius < 101:
                    cv2.putText(self.frame, "Number Of Balls:"+"One contour 2 balls", (0,15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (34, 248, 224),2)
                    regionNumber.region_number(self)
                elif self.radius > 101 and self.radius < 150:
                    cv2.putText(self.frame,"Number Of Balls:"+" One contour 3 balls: ",(0,15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (34, 248, 224), 2)
                    regionNumber.region_number(self)

            elif len(self._cnts) == 2 and self.radius > 55 and self.radius < 101:

                cv2.putText(self.frame, "Number Of Balls:"+"2 contour 3 ball ",(0,15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (34,248,224), 2)

                regionNumber.region_number(self)

            elif len(self._cnts) == 2 and self.radius < 55:
                # ilk topun kordinatı

                cv2.putText(self.frame,"Number Of Balls:"+"2", (0,15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (34,248,224), 2)


                regionNumber.region_number(self)


            elif len(self._cnts) == 3:

                cv2.putText(self.frame,"Number Of Balls:"+ "3 ",(0,15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (34, 248, 224), 2)


                regionNumber.region_number(self)

            general_control.centroid(self)
            cv2.imshow("mask", self.res)
            cv2.imshow("OpenCV Detection-180444003", self.frame)

            key = cv2.waitKey(1) & 0xFF

            if key == 27:
                break

    def balls_coordinates(self):
        for key, value in self.upper.items():  # upper means upper colors ,# key=green,yellow   Value(86, 255, 255),(54, 255, 255)
            core = np.ones((9, 9), np.uint8)  # Return a new array of 9x9, filled with ones.
            mask = cv2.inRange(self.hsv, self.lower[key], self.upper[key])  # Mask in Range loower and upper collors
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                                    core)  # It is the difference between dilation and erosion of an image.
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, core)
            # find contours in the mask and initialize the current
            self._cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

            for contour in self._cnts:
                if len(self._cnts) > 0:
                    regionNumber.centroid(self)
                    # print(self.radius)
                    if self.radius > 0.5 and self.radius < 55:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                        if cv2.contourArea(contour) < 1000:
                            continue
                        ((x, y), self.radius) = cv2.minEnclosingCircle(contour)

                        cv2.circle(self.frame, (int(x), int(y)), int(self.radius), self.colors[key], 2)
                        strXY = str(int(x)) + ', ' + str(int(y))
                        cv2.putText(self.frame, strXY, (int(x), int(y)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)


                    elif self.radius > 55 and self.radius < 101:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                        if cv2.contourArea(contour) < 1000:
                            continue
                        ((x, y), self.radius) = cv2.minEnclosingCircle(contour)

                        cv2.circle(self.frame, (int(x), int(y)), int(self.radius), self.colors[key], 2)
                        strXY = str(int(x)) + ', ' + str(int(y))
                        cv2.putText(self.frame, strXY, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),
                                    2)

                    elif self.radius > 101 and self.radius < 150:
                        # draw the circle and centroid on the frame,
                        # then update the list of tracked points
                        if cv2.contourArea(contour) < 1000:
                            continue
                        ((x, y), self.radius) = cv2.minEnclosingCircle(contour)
                        cv2.circle(self.frame, (int(x), int(y)), int(self.radius), self.colors[key], 2)
                        strXY = str(int(x)) + ', ' + str(int(y))
                        cv2.putText(self.frame, strXY, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0),
                                    2)

    def centroid(self):
        self._centers=[]
        self.c = max(self._cnts, key=cv2.contourArea)
        ((self.x, self.y), self.radius) = cv2.minEnclosingCircle(self.c)
        for i in range(len(self._cnts)):

            M = cv2.moments(self._cnts[i])
            self._centers.append((int(M['m10']/M['m00']), int(M['m01']/M['m00'])))



        #print(self._centers)  # IT PRINTS BALL'S COORDINATES ALSO REGION'S COORDINATES !


class general_control(regionNumber):

    def centroid(self):
        for key, value in self.upper.items():  # upper means upper colors ,# key=green,yellow   Value(86, 255, 255),(54, 255, 255)
            core = np.ones((9, 9), np.uint8)  # Return a new array of 9x9, filled with ones.
            mask = cv2.inRange(self.hsv, self.lower[key], self.upper[key])  # Mask in Range loower and upper collors
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                                    core)  # It is the difference between dilation and erosion of an image.
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, core)
            # find contours in the mask and initialize the current
            self.res = cv2.bitwise_and(self.frame, self.frame, mask=mask)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            center = None

            for contour in cnts:
                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                # print(approx)
                cv2.drawContours(self.frame, [approx], 0, (0, 0, 255), 2)
                x = approx.ravel()[0]  # bütün şekillerin x'deki köşelerini alır
                y = approx.ravel()[1] - 10  # ""
                self._centers = []

                for i in range(len(cnts)):
                    M = cv2.moments(cnts[i])
                    self._centers.append((int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])))

                    #print("center X : '{}'".format(round(M['m10'] / M['m00'])))
                    #print("center Y : '{}'".format(round(M['m01'] / M['m00'])))
                    if len(self._cnts) == 1:
                        for i in range(0, 1):
                            cv2.putText(self.res, "centroid coordinates of the green pixels= " + str(self._centers[i]),
                                        (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),
                                        2)

                    elif len(self._cnts) == 2:
                        if i in range(1,2):

                            cv2.putText(self.res,
                                    "centroid coordinates of the green pixels 1= " + str(self._centers[i-1]),
                                    (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),
                                    2)

                            cv2.putText(self.res, "centroid coordinates of the green pixels 2= " + str(self._centers[i]),
                                    (15, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),
                                    2)





                    cv2.circle(self.res, (round(M['m10'] / M['m00']), round(M['m01'] / M['m00'])), 5, (255, 0, 0),#IT SHOWS CENTROID OF GREEN PIXELS
                               -1)

        cv2.imshow("mask",self.res)
def main():
    a = regionNumber()
    a.number_of_balls()
    b = general_control()
    b.centroid()

#main()




#TKINTERRR

def exit():
    root.destroy()

def startIsPressed():
    exit()
    main()



root=Tk()
root.geometry("600x600")
root.title("OPENCV DETECTION BY UMUTCAN GUNGOR")
root.resizable(0,0)
root.config(bg="#ffffff")

HeadingLabel=tkinter.Label(root,text="Welcome to My OpenCv Project ! !",fg="blue",bg="gold",font = ("arial",15,"bold"),background="#ffffff")
HeadingLabel.pack()

id=tkinter.Label(root,text="180444003",fg="blue",font="Arial 16 bold",background="#ffffff")
id.place(x=235,y=50)

img="images/me.jpeg"
my_img=ImageTk.PhotoImage(Image.open(img))
ImageLabel=tkinter.Label(root,image=my_img).place(x=210,y=100)

img2=PhotoImage(file="images/start.png")

btnStart=Button(root,image=img2,relief=FLAT,border=0,background="#ffffff",command=startIsPressed)
btnStart.pack(pady=(300,0))

lblInstruction=Label(root,text="Click Start When You Ready \n Esc to Exit \n Pls try it 1 meter away from the camera for best results ! ",background="#ffffff",font=("Concolas",14),justify="center")
lblInstruction.pack(pady=(15,70))


lblRules=Label(root,text="If you liked it, please report your feedback by mail. Have fun ! \n umutcangungor@hotmail.com "
                         ,width=100,font=("Times",14),background="#000000",foreground="#FACA2F")
lblRules.pack()



root.mainloop()