from fastapi import APIRouter, Depends, status, HTTPException
from schemas.interaction import DrugInteractionInput
from core.checker import predict_interaction

router = APIRouter()

@router.post("/interaction_checker")
def get_prediction(data: DrugInteractionInput):
    try:
        result = predict_interaction(data.drugA, data.drugB)
        return {"input": data.dict(), "prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))