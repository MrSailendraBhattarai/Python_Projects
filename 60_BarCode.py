
# Bar Code
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    # Choose barcode type (EAN13, Code128, etc.)
    code128 = barcode.get_barcode_class('code128')
    
    # Generate the barcode
    barcode_instance = code128(data, writer=ImageWriter())
    
    # Save the barcode as an image (PNG format by default)
    barcode_instance.save(filename)

# Example usage
data = "123456789012"  # Barcode data (must be a valid barcode value, like EAN-13 or Code128)
filename = "barcode_example"  # Name of the output file (without extension)
generate_barcode(data, filename)
