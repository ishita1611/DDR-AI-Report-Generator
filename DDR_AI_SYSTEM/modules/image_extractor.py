import fitz
import os

def extract_images(pdf_path, output_folder):

    doc = fitz.open(pdf_path)

    os.makedirs(output_folder, exist_ok=True)

    images_by_page = {}

    for page_index in range(len(doc)):

        page = doc[page_index]
        image_list = page.get_images(full=True)

        images_by_page[page_index] = []

        largest_image = None
        largest_area = 0

        for img in image_list:

            xref = img[0]
            base_image = doc.extract_image(xref)

            width = base_image["width"]
            height = base_image["height"]

            area = width * height

            # keep largest image only
            if area > largest_area:
                largest_area = area
                largest_image = base_image["image"]

        if largest_image:

            image_name = f"page{page_index}.png"
            image_path = os.path.join(output_folder, image_name)

            with open(image_path, "wb") as f:
                f.write(largest_image)

            images_by_page[page_index].append(image_path)

    return images_by_page