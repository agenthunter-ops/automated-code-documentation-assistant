import pytest
from src.agents.doc_generator import generate_docstring


@pytest.mark.asyncio
async def test_generate_docstring(monkeypatch):
    async def fake_llm(code):
        return '"""Adds two numbers.\n\nArgs:\n  a (int): left operand\n  b (int): right operand\n\nReturns:\n  int: sum of a and b\n"""'

    # Monkeypatch internal LLM call
    monkeypatch.setattr("src.agents.doc_generator._llm.achat", lambda msgs: type("Resp", (), {"content": fake_llm(None)}))

    code = "def add(a: int, b: int):\n    return a + b"
    doc = await generate_docstring(code)
    assert "Adds two numbers" in doc
    assert "Returns:" in doc
