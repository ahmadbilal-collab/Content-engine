"""
Configuration module for AI Thought Leadership Engine.
Contains brand voice, content dimensions, and audience definitions.
"""

from .brand_config import BRAND_CONFIG, VOICE_GUIDELINES, SIGNATURE_PHRASES
from .dimensions_config import CONTENT_DIMENSIONS, TOPIC_AREAS
from .audiences_config import TARGET_AUDIENCES, AUDIENCE_TIERS

__all__ = [
    "BRAND_CONFIG",
    "VOICE_GUIDELINES",
    "SIGNATURE_PHRASES",
    "CONTENT_DIMENSIONS",
    "TOPIC_AREAS",
    "TARGET_AUDIENCES",
    "AUDIENCE_TIERS",
]
