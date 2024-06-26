"""Unit tests for Generative Agents scoring module."""

from langchain.llms.fake import FakeListLLM

from agential.cog.modules.score.generative_agents import (
    GenerativeAgentScorer,
)


def test_generative_agent_scorer() -> None:
    """Test GenerativeAgentScorer."""
    llm = FakeListLLM(responses=["1"])
    scorer = GenerativeAgentScorer(llm=llm)
    scores = scorer.score(
        memory_contents="Some memory.", relevant_memories="some relevant memories."
    )
    assert type(scores) is list
    assert len(scores) == 1
    assert type(scores[0]) == float
    assert scores[0] == 0.015


def test_generative_agent_scorer_clear() -> None:
    """Test GenerativeAgentScorer clear method."""
    llm = FakeListLLM(responses=["1"])
    scorer = GenerativeAgentScorer(llm=llm)
    scorer.clear()
    assert scorer.llm
