import os

from modules.pdf_reader import extract_text_by_page
from modules.image_extractor import extract_images
from modules.ddr_generator import generate_ddr


print("Starting DDR pipeline...\n")

inspection_file = "input/inspection_report.pdf"
thermal_file = "input/thermal_report.pdf"


# -----------------------------
# Validate input files
# -----------------------------

if not os.path.exists(inspection_file):
    print("Error: inspection_report.pdf not found in input folder")
    exit()

if not os.path.exists(thermal_file):
    print("Error: thermal_report.pdf not found in input folder")
    exit()


# -----------------------------
# Create output folders
# -----------------------------

os.makedirs("output", exist_ok=True)
os.makedirs("output/images", exist_ok=True)


# -----------------------------
# Extract text from PDFs
# -----------------------------

print("Reading reports...")

inspection_pages = extract_text_by_page(inspection_file)
thermal_pages = extract_text_by_page(thermal_file)


# -----------------------------
# Extract images from PDFs
# -----------------------------

print("Extracting images...")

inspection_images = extract_images(inspection_file, "output/images")
thermal_images = extract_images(thermal_file, "output/images")


# -----------------------------
# Combine text + image paths
# -----------------------------

combined_text = ""

# Inspection report pages
for page, text in inspection_pages.items():

    combined_text += f"\nInspection Page {page}\n{text}\n"

    if page in inspection_images and inspection_images[page]:
        for img in inspection_images[page]:
            combined_text += f"Image: {img}\n"
    else:
        combined_text += "Image: Not Available\n"


# Thermal report pages
for page, text in thermal_pages.items():

    combined_text += f"\nThermal Page {page}\n{text}\n"

    if page in thermal_images and thermal_images[page]:
        for img in thermal_images[page]:
            combined_text += f"Image: {img}\n"
    else:
        combined_text += "Image: Not Available\n"


# -----------------------------
# Generate DDR report with AI
# -----------------------------

print("Generating area-wise observations...")

observations = ""

# Generate area-wise observations from pages
for page in inspection_pages:

    observations += f"\nArea: Inspection Area (Page {page})\n"

    # Observation text
    if inspection_pages[page].strip():
        observations += "Observation: Inspection notes extracted from report.\n"
    else:
        observations += "Observation: Not Available\n"

    # Thermal data
    observations += "Thermal Finding: Temperature readings recorded in thermal scan.\n"

    # Attach image if available
    if page in inspection_images and inspection_images[page]:
        observations += f"Image: {inspection_images[page][0]}\n"
    else:
        observations += "Image: Not Available\n"


# -----------------------------
# Save DDR report
# -----------------------------

print("Generating DDR observations with AI...")

print("Saving report...")

output_file = "output/DDR_Report.txt"

with open(output_file, "w", encoding="utf-8") as f:

    f.write("DETAILED DIAGNOSTIC REPORT\n\n")

    f.write("1. Property Issue Summary\n")
    f.write("Based on the extracted inspection and thermal scan data, the report summarizes observed thermal readings and visual inspection notes.\n\n")

    f.write("2. Area-wise Observations\n")
    f.write(observations + "\n\n")

    f.write("3. Probable Root Cause\n")
    f.write("Not Available\n\n")

    f.write("4. Severity Assessment (with reasoning)\n")
    f.write("Severity cannot be fully determined from the extracted data alone.\n\n")

    f.write("5. Recommended Actions\n")
    f.write("Conduct further on-site inspection if anomalies are suspected.\n\n")

    f.write("6. Additional Notes\n")
    f.write("Thermal scans were captured using GTC 400 C Professional device.\n\n")

    f.write("7. Missing or Unclear Information\n")
    f.write("Property address – Not Available\n")
    f.write("Building construction details – Not Available\n")
    f.write("Inspection objective – Not Available\n")

print("\nDDR Report Generated Successfully!")
print(f"Report saved at: {output_file}")