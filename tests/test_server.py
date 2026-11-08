from src.server.server import Server
import pytest 


def test_guesses():
    #Server instance
    st : Server = Server("chess")
    assert st.guess("cass", True) == (['R','R','R','R','R'], '1')
    assert st.guess("c1ess", True) == (['R','R','R','R','R'], '2')
    assert st.guess("heron", True) == (['Y','Y','R','R','R'], 'INCOMPLETE')
    assert st.guess("chees", True) == (['G','G','G','R','G'], 'INCOMPLETE')
    assert st.guess("CHESS", True) == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("chess", True) == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("sssss", True) == (['R','R','R','G','G'], 'INCOMPLETE')
    st.setWord("wendy")
    assert st.guess("wendy", True) == (['G','G','G','G','G'], 'SUCCESS')
    assert st.guess("windy", True) == (['G','R','G','G','G'], 'INCOMPLETE')
    assert st.guess("wwwww", True) == (['G','R','R','R','R'], 'INCOMPLETE')
    st.setWord("caves")
    assert st.guess("chess", True) == (['G','R','Y','R','G'], 'INCOMPLETE')
    st.setWord("HELLO")
    assert st.guess("HILLO", True) == (['G','R','G','G','G'], 'INCOMPLETE')
