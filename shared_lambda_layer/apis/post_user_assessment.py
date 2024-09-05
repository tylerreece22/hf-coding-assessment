from typing import Literal

from pydantic import BaseModel, EmailStr


class UserAssessmentRequestBody(BaseModel):
    id: str
    full_name: str
    """
    First name and last name (ex. John Doe)
    """
    email: EmailStr
    phone: str
    """
    Any format. This is a magic api with no flaws XD
    """
    full_address: str
    """
    Example: 221B Baker Street, London, England
    """
    ipv4: str
    """
    Ip address of the client making the request to the api
    """


class MappedPostUserAssessmentResponse(UserAssessmentRequestBody):
    id: str
    fullName: str
    """
    First name and last name (ex. John Doe)
    """
    email: EmailStr
    phone: str
    """
    Any format. This is a magic api with no flaws XD
    """
    fullAddress: str
    """
    Example: 221B Baker Street, London, England
    """
    ipv4: str
    """
    Ip address of the client making the request to the api
    """
    riskRating: Literal["high", "medium", "low"]


def post_user_assessment(
    body: UserAssessmentRequestBody,
) -> MappedPostUserAssessmentResponse:
    """
    This is just a mocked function but you can
    pretend it is making a request to an api

    :param body: UserAssessmentRequestBody
    :return: MappedPostUserAssessmentResponse
    """
    if body.id % 2 == 0:
        return MappedPostUserAssessmentResponse(
            **{
                "id": body.id,
                "fullName": body.full_name,
                "email": body.email,
                "phone": body.phone,
                "fullAddress": body.full_address,
                "ipv4": body.ipv4,
                "riskRating": "high",
            }
        )
    elif body.id % 3 == 0:
        return MappedPostUserAssessmentResponse(
            **{
                "id": body.id,
                "fullName": body.full_name,
                "email": body.email,
                "phone": body.phone,
                "fullAddress": body.full_address,
                "ipv4": body.ipv4,
                "riskRating": "medium",
            }
        )
    else:
        return MappedPostUserAssessmentResponse(
            **{
                "id": body.id,
                "fullName": body.full_name,
                "email": body.email,
                "phone": body.phone,
                "fullAddress": body.full_address,
                "ipv4": body.ipv4,
                "riskRating": "low",
            }
        )
