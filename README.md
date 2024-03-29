# RoadmapGPT
Get a roadmap and never get lost again. RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better. RoadmapGPT aims to be an LLM alternative to [roadmap.sh](https://roadmap.sh).

![image](https://github.com/robinroy03/RoadmapGPT/assets/115863770/0b4460a9-80b1-4032-ae38-31990ea0aecb)

## TODO

- [X] Make a website which outputs something good enough.
- [X] Parsers to parse the output.
- [X] A Google sheet to store all user prompts.
- [ ] There is this weird rectangle in the output, got to fix that bug.

## How to run

Go to the root directory and type 
```
streamlit run main.py
```

Add a folder named `.streamlit` with `secrets.toml` and add your TOKEN as `TOKEN = whatever_your_token`
You also need a google cloud service account to store prompts.

Format of `secrets.toml`:
```
TOKEN = 

[gspread_credentials]
"type" = "service_account"
...
...

"universe_domain" = "googleapis.com"
```
You could get the gspread credentials by following [this](https://docs.streamlit.io/knowledge-base/tutorials/databases/private-gsheet)

The basic version of the application is written with streamlit. It'll be a lot more flexible if done with js.