from sqlalchemy import Column, Integer, Text, DateTime, String, Index, func

from .db import Base, engine


class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(Text)
    created_date = Column(DateTime)
    rubrics = Column(String(255))

    __table_args__ = (
        Index(
            'ix_examples_tsv',
            func.to_tsvector('russian', text),
            postgresql_using='gin'
        ),
    )



