from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_cusco():
    result = get_local_culture_info("Cusco")
    assert result["status"] == "success"
    assert len(result["dishes"]) >= 1
    assert "Lomo Saltado" in result["dishes"]

def test_get_local_culture_info_default():
    result = get_local_culture_info("Madrid")
    assert result["status"] == "success"
    assert len(result["phrases"]) >= 1
