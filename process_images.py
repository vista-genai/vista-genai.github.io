from rembg import remove
from PIL import Image
import os

def make_transparent(input_path, output_path):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Successfully removed background from {input_path} and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create images directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")
        
    # Process first logo
    make_transparent("images/icdm_logo1.jpg", "images/icdm_logo1_transparent.png")
    
    # Process second logo
    make_transparent("images/icdm_logo2.jpg", "images/icdm_logo2_transparent.png") 