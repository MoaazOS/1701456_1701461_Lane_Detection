# Image Processing & Pattern Recognition Project
* Moaaz Osama Abd El_Mohymen    
 ID: 1701456
* Moatasem Mohie El_Deen        
 ID: 1701461
# Finding Lane Lines on the Road - Advanced Techniques

## Computer vision with OpenCV

#### When we drive, we use our eyes to decide where to go.  The lines on the road that show us where the lanes are, will act as our constant reference for where to steer the vehicle.  Naturally, one of the first things we would like to do in developing a self-driving car is to automatically detect lane lines using an algorithm.

#### In this project you will detect lane lines in images using Python and OpenCV.  OpenCV means "Open-Source Computer Vision", which is a package that has many useful tools for analyzing images.

---

**Advanced Lane Finding Project**

The goals/ steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to the center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Images References)

[image1]: ./my_images/15-image-pipeline-readme.png "Finding Lane Line"



![alt text][image1] 


---

## Code Files & Functionality

### 1. Files:

* **camera_calibration.py**  is the script used to analyze the set of chessboard images, and save the camera calibration coefficients (mtx,dist). That is the first step in the project.
* **perspective_transform.py** is the script used to choose the appropriate perspective transformation matrices (M, Minv) to convert images to bird's-eye view. That is the second step in the project.
* **load_parameters.py** contains the functions used to load camera coefficients (mtx, dist) and perspective matrices (M, Minv).
* **warp_transformer.py** contains the functions used to color transform, warp and create the binary images.
* **line.py** defines a class to keep track of lane line detection. This information helps the main pipeline code to decide if the current image frame is good or bad.
* **main.py** contains the script used to run the video pipeline and create the final annotated video.
* **[Annotated Project Video](https://vimeo.com/211246515)** Click on this link to watch the annotations for the project video.
* **[Annotated Challenge Video](https://vimeo.com/211246891)** Click on this link to watch the annotations for the challenge video!
* **writeup_report.md** is the summary report of the results



### 2. Functional codes:

#### Camera calibration:
Open the **camera_calibration.py** and set the proper output directory (code lines 8-17).

Default configuration will:
* Read calibration images from: `camera_cal`
* Save results to: `output_images/camera_cal` 

Execute the script as follow: 
```
python camera_calibration.py
```

#### Perspective Transform Matrices:
Open the **load_parameters.py** and set the proper income directories (code lines 5-11).

Default configuration will:
* Read camera coefficients from: `output_images/camera_cal`

Open the **perspective_transform.py** and set the proper output directory (code lines 12-21).

Default configuration will:
* Save warped straight road image for check to: `output_images/bird_eye_test`
* Save results perspective matrices to: `output_images/camera_cal`

Execute the script as follow: 
```
python perspective_transform.py
```
Modify the trapezoid ratios (code lines 28-31) until you are happy with the output bird's-eye image 


#### Video Pipeline:
Open the **load_parameters.py** and set the proper income directories (code lines 5-11).

Default configuration will:
* Read camera coefficients and perspective matrices from: `output_images/camera_cal`

Open the **main.py** and set the proper output directory and video source (code lines 303-304).

Default configuration will:
* Read video source from parent directory
* Save annotated video to: `output_images`

Execute the script as follow: 
```
python main.py
```


---





## Acknowledgments / References

* [Udacity Self-Driving Car Nanodegree](https://www.udacity.com/drive)
* [David A. Ventimiglia](http://davidaventimiglia.com/advanced_lane_lines.html)
* [Vivek Yadav](https://chatbotslife.com/robust-lane-finding-using-advanced-computer-vision-techniques-46875bb3c8aa)
