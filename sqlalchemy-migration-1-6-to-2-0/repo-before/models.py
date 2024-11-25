from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship, backref
from database import Base

class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", backref="publisher")

    # Define a composite index if you often query by both id and name together
    __table_args__ = (
        Index("ix_publishers_id_name", "id", "name"),
    )

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String)
    publisher_id = Column(Integer, ForeignKey("publishers.id"))

    # Define a composite index for frequent queries by title and author
    __table_args__ = (
        Index("ix_books_title_author", "title", "author"),
        Index("ix_books_publisher_id_title", "publisher_id", "title"),  # Example if you query by publisher and title
    )
