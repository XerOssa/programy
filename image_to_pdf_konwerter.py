from PIL import Image

def convert_images_to_pdf(jpg_filenames, pdf_filename):
    images = [Image.open(filename) for filename in jpg_filenames]
    images[0].save(pdf_filename, "PDF", resolution=100.0, save_all=True, append_images=images[1:])

# Przykładowe użycie
jpg_filenames = ["D:/ROBOTA/python/programy/wypis/wypis1_1.jpg", "D:/ROBOTA/python/programy/wypis/wypis1_2.jpg", "D:/ROBOTA/python/programy/wypis/wypis1_3.jpg", "D:/ROBOTA/python/programy/wypis/wypis1_4.jpg", "D:/ROBOTA/python/programy/wypis/wypis1_5.jpg", "D:/ROBOTA/python/programy/wypis/wypis1_6.jpg"]
pdf_filename = "D:/ROBOTA/mieszkanie/ANEKS/wypis/polaczony.pdf"
convert_images_to_pdf(jpg_filenames, pdf_filename)
