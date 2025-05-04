from pydantic import BaseModel, EmailStr, Field


class PatientCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=4)


class PatientUpdate(PatientCreate):
    pass


class ShowPatient(BaseModel):
    patient_id: int  # ✅
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
