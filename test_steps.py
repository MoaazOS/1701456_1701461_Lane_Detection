left_line = Line()
right_line = Line()
detected = False

img = cv2.imread(images[4])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
undistorted = cv2.undistort(img, mtx, dist, None, mtx)
binary_warped, binary_output2 = thresholding(undistorted, M)

if not detected:
    left_fit, right_fit, left_curverad, right_curverad, outimg = sliding_window(binary_warped)
    detected = True
else:
    left_fit, right_fit, left_curverad, right_curverad, _ = non_sliding(binary_warped, left_fit, right_fit)

result = draw_lane(undistorted, binary_warped, left_fit, right_fit, left_curverad, right_curverad)

# Display Images
f, axarr = plt.subplots(5, sharex=True, figsize=(14,5*8.3))
f.subplots_adjust(hspace=0.1, wspace=0.05)
axarr[0].imshow(img, cmap=None) 
axarr[0].set_title('Original', fontsize=20)
axarr[1].imshow(binary_output2, cmap='gray') 
axarr[1].set_title('Yellow White', fontsize=20)
axarr[2].imshow(binary_warped, cmap='gray') 
axarr[2].set_title('binary_warped', fontsize=20)
axarr[3].imshow(outimg, cmap='gray') 
axarr[3].set_title('window', fontsize=20)
axarr[4].imshow(result, cmap='gray') 
axarr[4].set_title('result', fontsize=20)
