# Bingo

Sovelluksen avulla käyttäjä pystyy luomaan tulostettavia bingolappuja. Jokaisen bingolapun tiedot tallennetaan tietokantaan ja niillä on oma numero. Sovelluksella voi tämän jälkeen arpoa bingonumerot ja se samalla tarkistaa löytyykö bingo jostain tulostetusta bingolapusta. Jos jossain bingolapussa on voitto, sovellus kertoo kyseisen bingolapun numeron.


## Dokumentaatio

[Käyttöohje](https://github.com/janneko01/ot-harjoitustyo/blob/main/Dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/janneko01/ot-harjoitustyo/blob/main/Dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/janneko01/ot-harjoitustyo/blob/main/Dokumentaatio/tuntikirjanpito.md)

[Changelog]([https://github.com/janneko01/ot-harjoitustyo/blob/main/Dokumentaatio/vaatimusmaarittely.md])


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston .pylintrc tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
