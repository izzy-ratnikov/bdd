Feature: AnimeGO
  As a web site,
  I want to find anime online,
  So I can watch anime.


  Scenario: Basic AnimeGO Site
    Given the AnimeGO home page is displayed
    When the user press the button anime
    Then results equal url anime page