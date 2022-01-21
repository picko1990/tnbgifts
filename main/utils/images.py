from .transactions import get_transactions
from main.models import Image


def get_owned_images(address):
    txs = get_transactions(recipient=address)
    memos = [tx["memo"].strip() for tx in txs]
    relevant_memos = [memo for memo in memos if memo.startswith("tnb_gifts_")]
    owned_images = Image.objects.filter(unique_id__in=relevant_memos)
    return owned_images
