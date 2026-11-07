from src.server.server import Server
import pytest 


def test_guesses():
    #Server instance
    st : Server = Server("chess")
    assert st.guess("cass") == (['N','N','N','N','N'], '1')
    assert st.guess("c1ess") == (['N','N','N','N','N'], '2')
    assert st.guess("heron") == (['E','E','N','N','N'], 'I')
    assert st.guess("chees") == (['T','T','T','N','T'], 'I')
    assert st.guess("CHESS") == (['T','T','T','T','T'], 'S')
    assert st.guess("chess") == (['T','T','T','T','T'], 'S')
    assert st.guess("sssss") == (['E','E','N','N','N'], 'I')
    st.setWord("wendy")
    assert st.guess("wendy") == (['T','T','T','T','T'], 'S')
    assert st.guess("windy") == (['T','N','T','T','T'], 'I')
    assert st.guess("wwwww") == (['T','N','N','N','N'], 'I')

