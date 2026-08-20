from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db_session
from app.modules.auth.schemas import UserRegisterRequest, UserRegisterResponse
from app.modules.auth.security import hash_password
from app.modules.users.models import User, UserProfile, UserPreference

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserRegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    payload: UserRegisterRequest,
    db: AsyncSession = Depends(get_db_session),
) -> UserRegisterResponse:
    email = str(payload.email).strip().lower()

    existing_user = await db.scalar(
        select(User).where(User.email == email)
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        )

    display_name = payload.display_name or email.split("@", 1)[0]

    user = User(
        email=email,
        password_hash=hash_password(payload.password),
        account_status="ACTIVE",
    )

    profile = UserProfile(
        display_name=display_name,
        phone_encrypted=None,
    )

    preferences = UserPreference(
        route_preference="BALANCED",
        checkin_frequency_minutes=15,
        escalation_contact_delay_seconds=120,
    )

    user.profile = profile
    user.preferences = preferences

    db.add(user)

    try:
        await db.commit()
        await db.refresh(user)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists.",
        )

    return UserRegisterResponse(
        user_id=str(user.user_id),
        email=user.email,
        account_status=user.account_status,
        display_name=display_name,
    )