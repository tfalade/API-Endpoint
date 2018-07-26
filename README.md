# API-Endpoint
Using that data from the csv file, it will produce a JSON API with the following endpoints:

GET http://your-service-here/counties 
Returns all counties with election results in the following format:

{
  "counties": [
    {
      "name": "Adair",
      "fips": "19001",
      "elections": [
        {
          "party": "Democratic",
          "results": [
            {"candidate": "Hillary Clinton", "votes": 113},
            {"candidate": "Bernie Sanders", "votes": 86},
            {"candidate": "Martin O'Malley","votes": 0}
          ]
        }
        {
          "party": "Republican",
          "results": [
            {"candidate": "Ted Cruz","votes": 104},
            {"candidate": "Donald Trump","votes": 104}
            ...
          ]
        }
      ]
    },
    {
      "name": "Adams",
      "fips": "19003",
      "elections": [
        ...
      ]
    }
  ]
}




GET http://your-service-here/counties?democratic_winner=Hillary%20Clinton&republican_winner=Ted%20Cruz
	Returns the above results, but filtered to only show counties where the specified candidate received the most votes (including ties).




GET /counties/19001
Returns the results for the county with the specified FIPS code.

{
  "name": "Adair",
  "fips": "19001",
  "elections": [
    {
      "party": "Democratic",
      "results": [
        {"candidate": "Hillary Clinton", "votes": 113},
        {"candidate": "Bernie Sanders","votes": 86},
        {"candidate": "Martin O'Malley","votes": 0}
      ]
    }
    {
      "party": "Republican",
      "results": [
        {"candidate": "Ted Cruz","votes": 104},
        {"candidate": "Donald Trump","votes": 104}
        ...
      ]
    }
  ]
}

