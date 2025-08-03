import cv2
import matplotlib.pyplot as plt
import os

# Load the image
image_path = 'photo.png'  # Changed from photo.jpg to photo.png
image = cv2.imread(image_path)

# Check if image was loaded successfully
if image is None:
    print(f"Error: Could not load the image {image_path}. Please check if the file exists and is a valid image.")
    exit(1)

print(f"Image loaded successfully. Size: {image.shape}")

# Convert to Grayscale, HSV, and LAB
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Save images
cv2.imwrite('photo_grayscale.jpg', gray)
cv2.imwrite('photo_hsv.jpg', hsv)
cv2.imwrite('photo_lab.jpg', lab)
print("Images saved successfully!")

# Display images (optional - comment out if you don't want windows)
try:
    cv2.imshow('Grayscale', gray)
    cv2.imshow('HSV', hsv)
    cv2.imshow('LAB', lab)
    print("Press any key to close the image windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"Could not display images: {e}")

# Plot histogram of grayscale image
try:
    plt.figure(figsize=(10, 6))
    plt.hist(gray.ravel(), bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.title('Grayscale Image Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.savefig('grayscale_histogram.png', dpi=300, bbox_inches='tight')
    print("Histogram saved as 'grayscale_histogram.png'")
    plt.show()
except Exception as e:
    print(f"Could not create histogram: {e}")