from src.server.main import Server
import pytest 


def test_guesses():
    #Server instance
    st : Server = Server("chess")
    assert st.guess("cass") == ['1']
    assert st.guess("c1ess") == ['2']
    assert st.guess("heron") == ['E','E','N','N','N']
    assert st.guess("chees") == ['T','T','T','N','T']
    assert st.guess("CHESS") == ['T','T','T','T','T']
    assert st.guess("chess") == ['T','T','T','T','T']
    assert st.guess("sssss") == ['E','E','N','N','N']
    st.setWord("wendy")
    assert st.guess("wendy") == ['T','T','T','T','T']
    assert st.guess("windy") == ['T','N','T','T','T']
    assert st.guess("wwwww") == ['T','N','N','N','N']

