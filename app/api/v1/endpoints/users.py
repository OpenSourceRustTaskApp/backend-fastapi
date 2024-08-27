from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_users():
    """ユーザー一覧を取得するAPI"""

    # ダミーのユーザーデータ（データベース未実装のため）
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"},
    ]
    return users
