from pydantic import BaseModel

class FormatedResponse(BaseModel):
    """
    This is the response format that the AI will return.
    """
    topic: str
    summary: str
    keywords: list[str]
    sources: list[str]
    tools_used: list[str]