from beer import get_beers

def test_get_beers():
    assert get_beers("salad") == ['Trashy Blonde', 'Pilsen Lager', 'Avery Brown Dredge', 'Arcade Nation', 'Mixtape 8', 'Vice Bier'], "Incorrect output list"

if __name__ == "__main__":
    test_get_beers()
    print("Everything passed")