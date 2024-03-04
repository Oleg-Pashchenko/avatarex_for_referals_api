from pydantic import BaseModel


class RegisterData(BaseModel):
    email: str
    password: str
    name: str


class LoginData(BaseModel):
    email: str
    password: str


class AccountInfoData(BaseModel):
    session_key: str


class ReferalsListData(BaseModel):
    session_key: str


class ReferalsAddData(BaseModel):
    referal_link: str
    avatarex_id: int


class AccountPaymentsListData(BaseModel):
    session_key: str


class AccountPaymentsAddData(BaseModel):
    avatarex_user_email: str
    amount: int

