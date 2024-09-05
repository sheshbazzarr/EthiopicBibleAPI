from pydantic import BaseModel
from typing import List

class Verse(BaseModel):
    text: str

class Chapter(BaseModel):
    chapter: str
    title: str
    verses: List[str]

class Book(BaseModel):
    title: str
    abbv: str
    chapters: List[Chapter]
