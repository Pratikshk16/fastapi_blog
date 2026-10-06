from pydantic import BaseModel, EmailStr, Field

class RegisterIn(BaseModel):
    username: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=8)

class NomineeIn(BaseModel):
    name: str
    email: EmailStr
    phone: str
    relation: str = "Family"

class ChatIn(BaseModel):
    message: str
    document_id: int | None = None
    language: str = "English"

class ActionIn(BaseModel):
    action_type: str
    document_id: int | None = None
    nominee_id: int | None = None
    amount: float | None = None
    description: str = ""

class ApprovalIn(BaseModel):
    decision: str
