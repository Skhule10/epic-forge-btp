
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.() == {"status": "healthy"}

def test_start_sap_ai_core_job():
    response = client.post("/sap-ai-core/start-job", ={"job_id": "12345"})
    assert response.status_code == 200
    assert response.() == {"status": "Job started", "job_id": "12345"}

def test_get_sap_ai_core_job_status():
    response = client.get("/sap-ai-core/job-status/12345")
    assert response.status_code == 200
    assert response.() == {"status": "Job completed", "job_id": "12345"}

def test_stop_sap_ai_core_job():
    response = client.post("/sap-ai-core/stop-job", ={"job_id": "12345"})
    assert response.status_code == 200
    assert response.() == {"status": "Job stopped", "job_id": "12345"}

def test_process_nlp_query():
    response = client.post("/process-nlp-query", ={"text": "Hello, assistant!"})
    assert response.status_code == 200
    assert response.() == {"response": "Processed response for query: Hello, assistant!"}
