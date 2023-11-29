from src.pre_built.counter import count_ocurrences


def test_counter():
    "Testa se a função count_ocurrences está funcionando corretamente"
    assert count_ocurrences("data/jobs.csv", "javascript") == 122

    assert count_ocurrences("data/jobs.csv", "python") == 1639

    "Testa se a contagem de palavras é case insensitive"

    assert count_ocurrences("data/jobs.csv", "Python") == count_ocurrences(
        "data/jobs.csv", "python"
    )

    "Testa a contagem de uma palavra que não existe no arquivo"
    assert count_ocurrences("data/jobs.csv", "inexistente") == 0
    "Testa uma falha de execução"
    try:
        count_ocurrences("data/jobs.csv", 1)
    except AttributeError:
        pass
