import pytest

@pytest.fixture(autouse=True)
def nums():
    # Método Before: inicializa os números
    print("\n-- Início do Gerkin integrado ao Pytest --")
    nums = {"a": 0, "b": 0, "resultado": None}
    yield nums
    # Método After: reseta para None
    nums["a"] = None
    nums["b"] = None
    nums["resultado"] = None
    print("-- Fim do Gerkin integrado ao Pytest --")
