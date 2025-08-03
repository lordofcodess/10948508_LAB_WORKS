import cv2
import os

# Check if the image file exists
if not os.path.exists('photo.png'):
    print("Error: photo.png not found in the current directory")
    exit(1)

# Load the image
image = cv2.imread('photo.png')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not load the image. Please check if photo.png is a valid image file.")
    exit(1)

print(f"Image loaded successfully. Size: {image.shape}")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Image converted to grayscale successfully")

# Save grayscale image
cv2.imwrite('photo_gray.jpg', gray_image)
print("Grayscale image saved as 'photo_gray.jpg'")

# Display original and grayscale images (optional - comment out if you don't want windows)
try:
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)
    print("Press any key to close the image windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(f"Could not display images: {e}")
    print("Grayscale image was still saved successfully.")