import asyncio
import aiofiles
import os
from pathlib import Path

current_dir = Path(__file__).parent
files_dir = current_dir.parent / "files"


class File_handling:
    def __init__(self, filename) -> None:
        self.filename = str(filename)
        self.file_path = os.path.join(files_dir, self.filename)

    async def Create_file(self) -> str:
        try:
            async with aiofiles.open(self.file_path, mode="x") as create_file:
                await create_file.write("")
                result = "Created " + self.filename
            return result

        except FileExistsError:
            result = f"{self.filename} file already exist!"
            return result

        except Exception as e:
            result = f"An error occurred while creating {self.filename}: {str(e)}"
            return result

    async def Read_file(self) -> str:
        try:
            async with aiofiles.open(self.file_path, mode="r") as read:
                content = await read.read()
                if not content.strip():
                    content = "File is empty!"
            return content

        except FileNotFoundError:
            result = self.filename + " file doesn't exist!"
            return result

        except Exception as e:
            result = f"An error occurred while reading {self.filename}: {str(e)}"
            return result

    async def Append_to_file(self, content) -> str:
        try:
            if not os.path.exists(self.file_path):
                return f"{self.filename} doesn't exist, please create it first."
            async with aiofiles.open(self.file_path, mode="a") as append:
                read_content = await self.Read_file()
                if read_content != "File is empty!":
                    await append.write("\n")
                result = await append.write(content)
                result = f"{result} letters appended"
            return result

        except Exception as e:
            result = f"An error occurred while appending to {self.filename}: {str(e)}"
            return result

    async def Write_to_file(self, content) -> str:
        try:
            if not os.path.exists(self.file_path):
                return f"{self.filename} doesn't exist, please create it first."
            async with aiofiles.open(self.file_path, mode="w") as write:
                result = await write.write(content)
                result = f"{result} letters written"
            return result

        except Exception as e:
            result = f"An error occurred while writing to {self.filename}: {str(e)}"
            return result
