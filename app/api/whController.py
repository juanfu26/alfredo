from fastapi import APIRouter
from .whSchema import DataRequest

router = APIRouter(
  tags=['Webhook']
)

@router.post('/webhook')
def webhook(data: DataRequest):
  return {
        "fulfillmentText": 'This is from the replit webhook',
        "source": 'webhook'
    }