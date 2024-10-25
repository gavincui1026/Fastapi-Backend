import hashlib

import sqlalchemy

from src.models.db.account import Account
from src.repository.crud.base import BaseCRUDRepository
from src.repository.oss import AmazonS3Repository, OSSRepository
from src.models.db.oss import Upload


class OSSCRUDRepository(BaseCRUDRepository):
    async def is_file_exist(self, hash: str) -> bool:
        result = await self.async_session.execute(sqlalchemy.select(Upload).where(Upload.file_hash == hash))
        result = result.scalar_one_or_none()
        return result is not None
    def get_oss_repo(self,name:str)->OSSRepository:
        repo_list = {
            'amazon_s3':AmazonS3Repository
        }
        return repo_list[name]()
    async def upload(self, key: str, file: bytes, user: Account) -> None:
        file_original_name = key
        amazon_s3_repo = self.get_oss_repo('amazon_s3')
        file_ext = key.split('.')[-1]
        # 计算文件的MD5值，防止重复上传
        file_md5 = hashlib.md5(file).hexdigest()
        key = file_md5
        # 支持的文件类型有图片、视频、音频、文档，pdf
        if file_ext not in ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'avi', 'mov', 'mp3', 'wav', 'doc', 'docx', 'pdf']:
            raise ValueError("Unsupported file type")
        amazon_s3_repo.upload(key=key, file=file)
        new_upload = Upload(
            file_name=file_original_name,
            file_ext=file_ext,
            file_size=len(file),
            file_hash=file_md5,
            uploader_id=user.id,
        )
        self.async_session.add(new_upload)
        await self.async_session.commit()

    async def download(self, key: str):
        amazon_s3_repo = self.get_oss_repo('amazon_s3')
        ext_result = await self.async_session.execute(sqlalchemy.select(Upload).where(Upload.file_hash == key))
        ext = ext_result.scalar_one_or_none()
        if not ext:
            raise ValueError("File not found")

        return amazon_s3_repo.download(key=key),ext.file_ext
