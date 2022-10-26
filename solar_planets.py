import cv2
img = cv2.imread("solar-system.jpg")
cv2.waitKey(0)

text_to_show = "Sun"
cv2.putText(img,
           text_to_show,
           (50,100),
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,
           color=(255,255,255)
           )


text_to_show = "Mercury"
cv2.putText(img,
            text_to_show,
            (80,190),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Venus"
cv2.putText(img,
            text_to_show,
            (190,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Earth"
cv2.putText(img,
            text_to_show,
            (280,170),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Mars"
cv2.putText(img,
            text_to_show,
            (370,190),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Jupiter"
cv2.putText(img,
            text_to_show,
            (490,80),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Saturn"
cv2.putText(img,
            text_to_show,
            (690,120),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )

text_to_show = "Uranus"
cv2.putText(img,
            text_to_show,
            (940,150),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )
text_to_show = "Neptune"
cv2.putText(img,
            text_to_show,
            (1100,160),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale=1,
            color=(255,255,255)
            )
cv2.imshow("output",img)
