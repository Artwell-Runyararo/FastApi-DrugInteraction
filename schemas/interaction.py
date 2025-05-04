from pydantic import BaseModel

class DrugInteractionInput(BaseModel):
    drugA: str
    drugB: str

    class Config:
        from_attributes = True
