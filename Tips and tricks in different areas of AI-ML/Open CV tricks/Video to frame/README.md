```python
def extractFrames(video):
    
    i, n = 1, 30
    
    cap = cv2.VideoCapture(video)

    frames = []

    if cap.isOpened()==False:
        print("Either file not found or wrong codec used")

    while cap.isOpened():
        ret, frame = cap.read()

        if ret==True:
            out = frame.copy()
            out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
            out = cv2.resize(out, (320, 240)).astype("float32")
            
            if i%n==0:
                frames.append(frame)
            
            i+=1

            if cv2.waitKey(1) & 0xFF==ord('q'):
                break

        # if nothing is returned, break out of the loop
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    
    return np.array(frames)
```
