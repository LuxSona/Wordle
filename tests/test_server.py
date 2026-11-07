from src.server.server import Server
import pytest 


def test_guesses():
    #Server instance
    st : Server = Server("chess")
    assert st.guess("cass") == (['R','R','R','R','R'], '1')
    assert st.guess("c1ess") == (['R','R','R','R','R'], '2')
    assert st.guess("heron") == (['Y','Y','R','R','R'], 'INCOMPLETE')
    assert st.guess("chees") == (['G','G','G','R','G'], 'INCOMPLETE')
    assert st.guess("CHESS") == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("chess") == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("sssss") == (['R','R','R','G','G'], 'INCOMPLETE')
    st.setWord("wendy")
    assert st.guess("wendy") == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("windy") == (['G','R','G','G','G'], 'INCOMPLETE')
    assert st.guess("wwwww") == (['G','R','R','R','R'], 'INCOMPLETE')
    st.setWord("caves")
    assert st.guess("chess") == (['G','R','Y','R','G'], 'INCOMPLETE')

