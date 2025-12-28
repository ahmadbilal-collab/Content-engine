"""
GEMINI CLIENT
Full integration with Google Gemini API including:
- Search grounding for real-time research
- Structured output generation
- Multiple model support
"""

import os
import json
from typing import Optional, Dict, Any, List
from dotenv import load_dotenv

try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

load_dotenv()


class GeminiClient:
    """
    Unified Gemini API client for the AI Thought Leadership Engine.
    Supports search grounding, structured output, and multiple models.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini client.

        Args:
            api_key: Optional API key. If not provided, uses GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gemini API key required. Set GEMINI_API_KEY environment variable "
                "or pass api_key parameter."
            )

        if not GENAI_AVAILABLE:
            raise ImportError(
                "google-genai package not installed. "
                "Run: pip install google-genai"
            )

        # Initialize the client
        self.client = genai.Client(api_key=self.api_key)

        # Model configurations
        self.models = {
            "flash": os.getenv("GEMINI_DEFAULT_MODEL", "gemini-2.0-flash-exp"),
            "pro": os.getenv("GEMINI_PRO_MODEL", "gemini-1.5-pro"),
        }

        # Default generation config
        self.default_config = types.GenerateContentConfig(
            temperature=0.7,
            top_p=0.95,
            max_output_tokens=8192,
        )

    def generate(
        self,
        prompt: str,
        model: str = "flash",
        temperature: float = 0.7,
        max_tokens: int = 8192,
        system_instruction: Optional[str] = None,
    ) -> str:
        """
        Generate content using Gemini.

        Args:
            prompt: The prompt to send to the model
            model: Model to use ("flash" or "pro")
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum output tokens
            system_instruction: Optional system instruction

        Returns:
            Generated text response
        """
        model_id = self.models.get(model, model)

        config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=0.95,
            max_output_tokens=max_tokens,
            system_instruction=system_instruction,
        )

        response = self.client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=config,
        )

        return response.text

    def research_with_search(
        self,
        prompt: str,
        model: str = "flash",
        temperature: float = 0.4,
    ) -> Dict[str, Any]:
        """
        Research using Gemini with Google Search grounding.
        Returns structured data with sources.

        Args:
            prompt: Research query/prompt
            model: Model to use
            temperature: Lower for factual research

        Returns:
            Dict with research results and sources
        """
        model_id = self.models.get(model, model)

        # Enable search grounding
        search_tool = types.Tool(
            google_search=types.GoogleSearch()
        )

        config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=0.95,
            max_output_tokens=8192,
            tools=[search_tool],
        )

        # Wrap prompt to request JSON output
        research_prompt = f"""
{prompt}

IMPORTANT: Return your findings as valid JSON with the following structure:
{{
    "findings": [...],
    "sources": [...],
    "summary": "..."
}}
"""

        response = self.client.models.generate_content(
            model=model_id,
            contents=research_prompt,
            config=config,
        )

        # Extract grounding metadata if available
        grounding_metadata = None
        if hasattr(response, 'candidates') and response.candidates:
            candidate = response.candidates[0]
            if hasattr(candidate, 'grounding_metadata'):
                grounding_metadata = candidate.grounding_metadata

        # Try to parse JSON from response
        try:
            result = self._extract_json(response.text)
        except (json.JSONDecodeError, ValueError):
            result = {
                "raw_response": response.text,
                "findings": [],
                "sources": [],
            }

        # Add grounding sources if available
        if grounding_metadata:
            result["grounding_sources"] = self._extract_grounding_sources(grounding_metadata)

        return result

    def generate_structured(
        self,
        prompt: str,
        schema: Dict[str, Any],
        model: str = "flash",
        temperature: float = 0.7,
    ) -> Dict[str, Any]:
        """
        Generate structured output conforming to a JSON schema.

        Args:
            prompt: The prompt for generation
            schema: JSON schema for the expected output
            model: Model to use
            temperature: Sampling temperature

        Returns:
            Parsed JSON object conforming to schema
        """
        model_id = self.models.get(model, model)

        # Create schema-guided prompt
        structured_prompt = f"""
{prompt}

You MUST respond with valid JSON that conforms to this schema:
{json.dumps(schema, indent=2)}

Return ONLY the JSON object, no additional text or markdown formatting.
"""

        config = types.GenerateContentConfig(
            temperature=temperature,
            top_p=0.95,
            max_output_tokens=8192,
            response_mime_type="application/json",
        )

        response = self.client.models.generate_content(
            model=model_id,
            contents=structured_prompt,
            config=config,
        )

        return self._extract_json(response.text)

    def analyze_url(
        self,
        url: str,
        analysis_prompt: str,
        model: str = "flash",
    ) -> Dict[str, Any]:
        """
        Analyze content from a URL using search grounding.

        Args:
            url: URL to analyze
            analysis_prompt: What to analyze about the content
            model: Model to use

        Returns:
            Analysis results
        """
        prompt = f"""
Analyze the content at this URL: {url}

{analysis_prompt}

Provide your analysis as JSON with:
{{
    "url": "{url}",
    "title": "...",
    "summary": "...",
    "key_points": [...],
    "analysis": "...",
    "relevance_to_ai_design": "..."
}}
"""
        return self.research_with_search(prompt, model=model)

    def _extract_json(self, text: str) -> Dict[str, Any]:
        """
        Extract JSON from text response, handling common formatting issues.
        """
        # Remove markdown code blocks if present
        text = text.strip()
        if text.startswith("```json"):
            text = text[7:]
        elif text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

        # Try to parse directly
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Try to find JSON object in text
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end > start:
            try:
                return json.loads(text[start:end])
            except json.JSONDecodeError:
                pass

        # Try to find JSON array
        start = text.find("[")
        end = text.rfind("]") + 1
        if start != -1 and end > start:
            try:
                return {"items": json.loads(text[start:end])}
            except json.JSONDecodeError:
                pass

        raise ValueError(f"Could not extract JSON from response: {text[:200]}...")

    def _extract_grounding_sources(self, grounding_metadata) -> List[Dict[str, str]]:
        """
        Extract sources from grounding metadata.
        """
        sources = []
        if hasattr(grounding_metadata, 'grounding_chunks'):
            for chunk in grounding_metadata.grounding_chunks:
                if hasattr(chunk, 'web'):
                    sources.append({
                        "title": getattr(chunk.web, 'title', 'Unknown'),
                        "uri": getattr(chunk.web, 'uri', ''),
                    })
        return sources

    def batch_generate(
        self,
        prompts: List[str],
        model: str = "flash",
        temperature: float = 0.7,
    ) -> List[str]:
        """
        Generate responses for multiple prompts.

        Args:
            prompts: List of prompts
            model: Model to use
            temperature: Sampling temperature

        Returns:
            List of generated responses
        """
        responses = []
        for prompt in prompts:
            response = self.generate(prompt, model=model, temperature=temperature)
            responses.append(response)
        return responses


# Convenience functions for module-level usage
_default_client: Optional[GeminiClient] = None


def get_client() -> GeminiClient:
    """Get or create the default Gemini client."""
    global _default_client
    if _default_client is None:
        _default_client = GeminiClient()
    return _default_client


def generate(prompt: str, **kwargs) -> str:
    """Generate content using the default client."""
    return get_client().generate(prompt, **kwargs)


def research(prompt: str, **kwargs) -> Dict[str, Any]:
    """Research with search grounding using the default client."""
    return get_client().research_with_search(prompt, **kwargs)
