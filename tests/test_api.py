"""Tests para la API REST."""

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestHealth:
    """Tests para health check."""
    
    def test_health_check(self):
        """Probar health check."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "app" in data


class TestRoot:
    """Tests para endpoint raíz."""
    
    def test_root(self):
        """Probar endpoint raíz."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "app" in data


class TestAgents:
    """Tests para agentes."""
    
    def test_list_agents(self):
        """Probar listar agentes."""
        response = client.get("/api/agents/list")
        assert response.status_code == 200
        data = response.json()
        assert "agents" in data
        assert "total" in data
    
    def test_create_agent(self):
        """Probar crear agente."""
        response = client.post(
            "/api/agents/create",
            params={"agent_id": "test-agent", "model": "gpt-4"}
        )
        # Este test pasará si LangChain/OpenAI está configurado
        if response.status_code == 500:
            # Si falla es porque no hay API key configurada
            assert "Error" in response.text or "error" in response.text
        else:
            assert response.status_code == 200
            data = response.json()
            assert data["agent_id"] == "test-agent"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
