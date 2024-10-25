from io import BytesIO

import fastapi

from src.api.dependencies.repository import get_repository
from src.api.dependencies.token import get_current_user
from src.models.db.account import Account
from src.repository.crud.oss import OSSCRUDRepository

router = fastapi.APIRouter(prefix="/documents", tags=["oss"])

@router.post(
    path="/upload",
    name="oss:upload",
    status_code=fastapi.status.HTTP_201_CREATED,
    description="Upload a document",
)
async def upload_document(
    file: fastapi.UploadFile = fastapi.File(...),
    current_user: Account = fastapi.Depends(get_current_user),
    oss_repo: OSSCRUDRepository = fastapi.Depends(get_repository(repo_type=OSSCRUDRepository)),
):
    if oss_repo.is_file_exist(file.filename):
        return fastapi.Response(status_code=fastapi.status.HTTP_201_CREATED, content="Document already exists!")
    try:
        await oss_repo.upload(key=file.filename, file=await file.read(), user=current_user)
    except ValueError as e:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=str(e))
    return fastapi.Response(status_code=fastapi.status.HTTP_201_CREATED, content="Document uploaded successfully!")

@router.get(
    path="/retrieve/{key}",
    name="oss:retrieve",
    description="Retrieve a document",
)
async def retrieve_document(
    key: str,
    oss_repo: OSSCRUDRepository = fastapi.Depends(get_repository(repo_type=OSSCRUDRepository)),
):
    file,ext = await oss_repo.download(key=key)
    return fastapi.responses.StreamingResponse(content=BytesIO(file), media_type=f"application/{ext}")


