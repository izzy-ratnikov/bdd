Feature: AnimeGO
  As a web site,
  I want to find anime online,
  So I can watch anime.


  Scenario: Basic AnimeGO Search
    Given the AnimeGO home page is displayed
    When the user searches for "naruto"
    Then results are shown for "naruto"