from app.services import auth_service


def test_password_hashing():
    pw = "correcthorsebatterystaple"
    h = auth_service.get_password_hash(pw)
    assert auth_service.verify_password(pw, h)


def test_jwt_roundtrip():
    token = auth_service.create_access_token(subject=123)
    payload = auth_service.decode_token(token)
    assert str(payload.get("sub")) == "123"
