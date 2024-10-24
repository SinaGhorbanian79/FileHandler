from pydantic import BaseModel


class File_requests(BaseModel):
    filename: str


class File_content_requests(File_requests):
    content: str
