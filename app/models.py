from pydantic import BaseModel


class Grade(BaseModel):
    grade: float


class Student(BaseModel):
    first_name: str
    last_name: str
    grade: float
