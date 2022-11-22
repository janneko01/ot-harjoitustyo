
classDiagram
    Pelaaja -- Ruutu
    Pelaaja -- Pelilauta
    Ruutu -- Pelilauta
    Pelilauta --|> Nopat

    class Pelaaja{
        nimi
        sijainti
    }
    class Ruutu{
        seuraavaRuutu()
    }
    class Nopat{
        noppienHeitto()
    }