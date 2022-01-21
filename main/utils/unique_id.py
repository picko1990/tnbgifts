import uuid


def generate_unique_id():
    return f"tnb_gifts_{uuid.uuid4().hex}"
