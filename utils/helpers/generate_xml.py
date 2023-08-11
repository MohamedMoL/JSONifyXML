import xml.etree.ElementTree as ET
from random import choice, uniform, randint
from loremipsum import get_sentences


def generate_book_data(book_id : int):
    author = f"Author{book_id}"
    title = f"Title{book_id}"
    genre = choice(["Computer", "Fantasy", "Romance", "Horror", "Science Fiction"])
    price = round(uniform(5, 50), 2)
    publish_date = f"{randint(2000, 2023)}-{randint(1, 12):02d}-{randint(1, 28):02d}"
    description = ' '.join(get_sentences(2))

    book_data = {
        "id": f"bk{book_id:05d}",
        "author": author,
        "title": title,
        "genre": genre,
        "price": str(price),
        "publish_date": publish_date,
        "description": description,
    }

    return book_data

def generate_catalog_xml(num_books : int):
    root = ET.Element("catalog")
    for i in range(1, num_books + 1):
        book_data = generate_book_data(i)
        book_element = ET.SubElement(root, "book", id=book_data["id"])

        ET.SubElement(book_element, "author").text = book_data["author"]
        ET.SubElement(book_element, "title").text = book_data["title"]
        ET.SubElement(book_element, "genre").text = book_data["genre"]
        ET.SubElement(book_element, "price").text = book_data["price"]
        ET.SubElement(book_element, "publish_date").text = book_data["publish_date"]
        ET.SubElement(book_element, "description").text = book_data["description"]

    return ET.tostring(root, encoding="utf-8")

if __name__ == "__main__":
    num_books_to_generate = 50000

    xml_data = generate_catalog_xml(num_books_to_generate)

    with open("catalog.xml", "wb") as file:
        file.write(xml_data)

    print(f"{num_books_to_generate} books generated and saved to catalog.xml.")
