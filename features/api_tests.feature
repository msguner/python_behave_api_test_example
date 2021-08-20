Feature: Api tests feature

  Scenario: Basic api test with common api steps
  """
    - Tüm api'lere uygulayabileceğimiz spesific olmayan temel api stepleri ile oluşturulmuş basit bir test case
  """
    Given a request url is "https://vpic.nhtsa.dot.gov/api"
    And add path "vehicles"
    And add path "getallmanufacturers"
    And add parameter format = json
    And add header key="Content-type" and value="application/json"
    When send get request
    Then the response status code is "200"

  Scenario: Get all vehicle manufacturers from nhtsa api and filter by country
  """
    - step 1: nhtsa api'ye istek atılarak tüm üretici firmalar çekilir.
    - step 2: Daha sonra bu çekilen firmalar ülkeye göre filtrelenir.
    - step 3: Filtrelenen üreticilerin sayısı kontrol edilir.
    - step 4: Filtrelenen üreticilerin markaları kontrol edilir.
  """
    Given get all vehicle manufacturers from nhtsa api
    When the response status code is "200"
    And get filtered vehicle manufacturers by country "JAPAN"
    Then verify that there are "5" manufacturers
    And verify filtered manufacturers common names are "Honda,Nissan,Mazda,Mitsubishi,Toyota"

  Scenario Outline: Get all vehicle manufacturers from nhtsa api and filter by common name
  """
    - step 1: nhtsa api'ye istek atılarak tüm üretici firmalar çekilir.
    - step 2: Daha sonra bu çekilen firmalar markaya(common name) e göre filtrelenir.
    - step 3: Filtrelenen üreticilerin sayısı kontrol edilir.
  """
    Given get all vehicle manufacturers from nhtsa api
    When the response status code is "200"
    And get filtered vehicle manufacturers by manufacturer common name "<name>"
    Then verify that there are "<count>" manufacturers
    Examples:
      | name  | count |
      | Ford  | 4     |
      | Tesla | 1     |
      # Hatalı case örneği (gelen count 5)
      | Honda | 1     |
