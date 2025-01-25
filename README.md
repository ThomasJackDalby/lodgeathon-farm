# lodgeathon-farm

## idea

general idea is to have a persistent "farm" which users control their farmers via a REST API, issuing commands.

e.g.
{
    "token" : "kjh3g45kj3h4g",
    "commands" : [
        { "type" : "move", "direction" : "left" },
        { "type" : "move", "direction" : "up" },
        { "type" : "dig" },
    ]
}