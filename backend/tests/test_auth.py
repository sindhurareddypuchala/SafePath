from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def unique_email():
    return f"auth-test-{uuid4().hex}@safepath.com"


def test_register_user_success(client, unique_email):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": unique_email,
            "password": "SafePath_Test_123!",
            "display_name": "Auth Test User",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert "user_id" in data
    assert data["email"] == unique_email
    assert data["account_status"] == "ACTIVE"
    assert data["display_name"] == "Auth Test User"

    assert "password" not in data
    assert "password_hash" not in data


def test_register_user_invalid_email(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "not-an-email",
            "password": "SafePath_Test_123!",
            "display_name": "Invalid Email User",
        },
    )

    assert response.status_code == 422


def test_register_user_weak_password(client, unique_email):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": unique_email,
            "password": "123",
            "display_name": "Weak Password User",
        },
    )

    assert response.status_code == 422


def test_register_duplicate_email(client, unique_email):
    payload = {
        "email": unique_email,
        "password": "SafePath_Test_123!",
        "display_name": "Duplicate Test User",
    }

    first_response = client.post(
        "/api/v1/auth/register",
        json=payload,
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/api/v1/auth/register",
        json=payload,
    )

    assert second_response.status_code == 409


def test_login_success(client, unique_email):
    password = "SafePath_Login_123!"

    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "email": unique_email,
            "password": password,
            "display_name": "Login Test User",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": unique_email,
            "password": password,
        },
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert data["token_type"] == "bearer"
    assert isinstance(data["access_token"], str)
    assert len(data["access_token"]) > 0


def test_login_wrong_password(client, unique_email):
    password = "SafePath_Login_456!"

    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "email": unique_email,
            "password": password,
            "display_name": "Wrong Password User",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": unique_email,
            "password": "WrongPassword_123!",
        },
    )

    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Invalid email or password."


def test_login_nonexistent_user(client):
    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": f"missing-{uuid4().hex}@safepath.com",
            "password": "SafePath_Test_123!",
        },
    )

    assert login_response.status_code == 401
    assert login_response.json()["detail"] == "Invalid email or password."