# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from typing import List

# Initialize the app and create database tables
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Dependency for the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility Functions
def get_book_or_404(book_id: int, db: Session):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# Filter Endpoints

@app.get("/books/search/title", response_model=List[schemas.Book])
def search_books_by_title(title: str, db: Session = Depends(get_db)):
    """Filter books by partial title match using `filter`."""
    books = db.query(models.Book).filter(models.Book.title.ilike(f"%{title}%")).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found with the given title")
    return books

@app.get("/books/search/author", response_model=List[schemas.Book])
def search_books_by_author(author: str, db: Session = Depends(get_db)):
    """Filter books by exact author match using `filter_by`."""
    books = db.query(models.Book).filter_by(author=author).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found for the given author")
    return books

@app.get("/publishers/search/name/exact", response_model=List[schemas.Publisher])
def search_publishers_by_name_exact(name: str, db: Session = Depends(get_db)):
    """Filter publishers by exact name match using `filter_by`."""
    publishers = db.query(models.Publisher).filter_by(name=name).all()
    if not publishers:
        raise HTTPException(status_code=404, detail="No publishers found with the given name")
    return publishers

@app.get("/publishers/search/name/partial", response_model=List[schemas.Publisher])
def search_publishers_by_name_partial(name: str, db: Session = Depends(get_db)):
    """Filter publishers by partial name match using `filter`."""
    publishers = db.query(models.Publisher).filter(models.Publisher.name.ilike(f"%{name}%")).all()
    if not publishers:
        raise HTTPException(status_code=404, detail="No publishers found matching the given name")
    return publishers

@app.get("/books/advanced-filter", response_model=List[schemas.Book])
def advanced_filter_books(
    author: Optional[str] = None,
    title: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Advanced filtering for books using both author and title as optional filters.
    """
    query = db.query(models.Book)
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    books = query.all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found matching the criteria")
    return books

# CRUD Operations

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return db_book

@app.post("/publishers/", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = models.Publisher(**publisher.dict())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

@app.get("/publishers/", response_model=List[schemas.Publisher])
def read_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    publishers = db.query(models.Publisher).offset(skip).limit(limit).all()
    return publishers

@app.get("/publishers/{publisher_id}", response_model=schemas.Publisher)
def read_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@app.put("/publishers/{publisher_id}", response_model=schemas.Publisher)
def update_publisher(publisher_id: int, publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if not db_publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    for key, value in publisher.dict().items():
        setattr(db_publisher, key, value)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

@app.delete("/publishers/{publisher_id}", response_model=schemas.Publisher)
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if not db_publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    db.delete(db_publisher)
    db.commit()
    return db_publisher

