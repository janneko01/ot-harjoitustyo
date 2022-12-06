# Bingo

Sovelluksen avulla käyttäjä pystyy luomaan tulostettavia bingolappuja. Jokaisen bingolapun tiedot tallennetaan tietokantaan ja niillä on oma numero. Sovelluksella voi tämän jälkeen arpoa bingonumerot ja se samalla tarkistaa löytyykö bingo jostain tulostetusta bingolapusta. Jos jossain bingolapussa on voitto, sovellus kertoo kyseisen bingolapun numeron.


## Dokumentaatio

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)


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