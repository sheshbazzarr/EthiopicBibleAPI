from fastapi import FastAPI, HTTPException
from typing import Optional
import json
import os
from schemas import Book, Chapter  

app = FastAPI(
    title="Ethiopic Bible API",
    description="An API for accessing the books of the Ethiopic Bible in Amharic.",
    version="1.0.0"
)

DATA_DIR = "Books/"

def load_book(book_name: str):
    file_path = os.path.join(DATA_DIR, f"{book_name.lower()}.json")
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Book not found")
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/book/{book_name}", response_model=Book, summary="Retrieve a Book")
async def get_book(book_name: str):
    """
     **Fetches a specific book by its name**. For example, use **'ኦሪት ዘፍጥረት'** to retrieve the book of Genesis. The book name should match the file name in the data directory (case-insensitive)
  
    - ኦሪት ዘፍጥረት
    - ኦሪት ዘጸአት
    - ኦሪት ዘሌዋውያን
    - ኦሪት ዘኍልቍ
    - ኦሪት ዘዳግም
    - መጽሐፈ ኢያሱ ወልደ ነዌ
    - መጽሐፈ መሣፍንት
    - መጽሐፈ ሩት
    - መጽሐፈ ሳሙኤል ቀዳማዊ
    - መጽሐፈ ሳሙኤል ካል
    - መጽሐፈ ነገሥት ቀዳማዊ
    - መጽሐፈ ነገሥት ካልዕ
    - መጽሐፈ ዜና መዋዕል ቀዳማዊ
    - መጽሐፈ ዜና መዋዕል ካልዕ
    - መጽሐፈ ዕዝራ
    - መጽሐፈ ነህምያ
    - መጽሐፈ አስቴር
    - መጽሐፈ ኢዮብ
    - መዝሙረ ዳዊት
    - መጽሐፈ ምሳሌ
    - መጽሐፈ መክብብ
    - መኃልየ መኃልይ ዘሰሎሞን
    - ትንቢተ ኢሳይያስ
    - ትንቢተ ኤርምያስ
    - ሰቆቃው ኤርምያስ
    - ትንቢተ ሕዝቅኤል
    - ትንቢተ ዳንኤል
    - ትንቢተ ሆሴዕ
    - ትንቢተ ኢዮኤል
    - ትንቢተ አሞጽ
    - ትንቢተ አብድዩ
    - ትንቢተ ዮናስ
    - ትንቢተ ሚክያስ
    - ትንቢተ ናሆም
    - ትንቢተ ዕንባቆም
    - ትንቢተ ሶፎንያስ
    - ትንቢተ ሐጌ
    - ትንቢተ ዘካርያስ
    - ትንቢተ ሚልክያ
    - የማቴዎስ ወንጌል
    - የማርቆስ ወንጌል
    - የሉቃስ ወንጌል
    - የዮሐንስ ወንጌል
    - የሐዋርያት ሥራ
    - ወደ ሮሜ ሰዎች
    - 1ኛ ወደ ቆሮንቶስ ሰዎች
    - 2ኛ ወደ ቆሮንቶስ ሰዎች
    - ወደ ገላትያ ሰዎች
    - ወደ ኤፌሶን ሰዎች
    - ወደ ፊልጵስዩስ ሰዎች
    - ወደ ቆላስይስ ሰዎች
    - 1ኛ ወደ ተሰሎንቄ ሰዎች
    - 2ኛ ወደ ተሰሎንቄ ሰዎች
    - 1ኛ ወደ ጢሞቴዎስ
    - 2ኛ ወደ ጢሞቴዎስ
    - ወደ ቲቶ
    - ወደ ፊልሞና
    - ወደ ዕብራውያን
    - የያዕቆብ መልእክት
    - 1ኛ የጴጥሮስ መልእክት
    - 2ኛ የጴጥሮስ መልእክት
    - 1ኛ የዮሐንስ መልእክት
    - 2ኛ የዮሐንስ መልእክት
    - 3ኛ የዮሐንስ መልእክት
    - የይሁዳ መልእክት
    - የዮሐንስ ራእይ
    """
    data = load_book(book_name)
    return data

@app.get("/book/{book_name}/chapter/{chapter_number}", response_model=Chapter, summary="Retrieve a Chapter", description="Fetches a specific chapter from a book by its chapter number. The chapter number should match the chapter identifier in the book's data.")
async def get_chapter(book_name: str, chapter_number: str):
    book = load_book(book_name)
    chapter = next((ch for ch in book['chapters'] if ch['chapter'] == chapter_number), None)
    if chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter

@app.get("/book/{book_name}/chapter/{chapter_number}/verse/{verse_number}", summary="Retrieve a Verse", description="Fetches a specific verse from a chapter in a book by its verse number. The verse number should be within the range of verses in the chapter.")
async def get_verse(book_name: str, chapter_number: str, verse_number: int):
    chapter = await get_chapter(book_name, chapter_number)
    if 0 <= verse_number < len(chapter['verses']):
        return {"verse": verse_number, "text": chapter['verses'][verse_number]}
    else:
        raise HTTPException(status_code=404, detail="Verse not found")
