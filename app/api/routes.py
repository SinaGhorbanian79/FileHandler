from fastapi import APIRouter, HTTPException
from app.services.file_service import File_handling
from app.model.models import File_requests, File_content_requests

router = APIRouter()


@router.post("/create_file")
async def create_file(file_op: File_requests):
    file_handle = File_handling(file_op.filename)
    result = await file_handle.Create_file()
    return {"message": result}


@router.post("/read_file")
async def read_file(file_op: File_requests):
    file_handle = File_handling(file_op.filename)
    result = await file_handle.Read_file()
    return {"message": result}


@router.post("/append_file")
async def append_file(file_op: File_content_requests):
    file_handle = File_handling(file_op.filename)
    result = await file_handle.Append_to_file(file_op.content)
    return {"message": result}


@router.post("/write_file")
async def write_file(file_op: File_content_requests):
    file_handle = File_handling(file_op.filename)
    result = await file_handle.Write_to_file(file_op.content)
    return {"message": result}
