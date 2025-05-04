from fastapi import APIRouter
from apis.v1 import (
    route_users,
    route_patients,
    route_locations,
    route_pharmacy,
    route_stock,
    route_pharmacystocks,
    route_auth,
    route_interaction
)


api_router = APIRouter()

api_router.include_router(route_pharmacy.router, prefix="/pharmacy", tags=["Pharmacies"])
api_router.include_router(route_users.router, prefix="/users", tags=["Users"])
api_router.include_router(route_stock.router, prefix="/stocks", tags=["Stocks/Medicines"])
api_router.include_router(route_patients.router, prefix="/patients", tags=["Patients"])
api_router.include_router(route_locations.router, prefix="/locations", tags=["Locations"])
api_router.include_router(route_pharmacystocks.router, prefix="/pharmacy_stocks", tags=["Pharmacy Stocks"])
api_router.include_router(route_auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(route_interaction.router, prefix="/drugs", tags=["Drug Interaction"])
