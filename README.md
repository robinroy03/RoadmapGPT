# RoadmapGPT
Get a roadmap and never get lost again. RoadmapGPT aims to give you a customized and comprehensive roadmap for all topics, helping you learn faster and better. See the image below for some ideas. Also, try this [bot I made](https://poe.com/Roadmap) to better understand what this is. I believe that if done properly, this could be useful rather than "yet-another-useless-API-wrapper"

![image](https://github.com/robinroy03/RoadmapGPT/assets/115863770/1a39d6f0-54fe-4cd2-9cf6-0188d135d0b2)

## TODO

- [X] Host the website 
- [X] ~~A better graph rendering (If you're a js developer and interested, make a PR)~~ 
Now we have a mermaid.js rendering done. But it got this weird rectangle in the graph for some reason. Got to fix that.
- [ ] Improve the backend with better prompts, asking the user to give topics he is familiar with already to make it more customizable.

## How to run

Go to the root directory and type 
```
$streamlit run main.py
```

The basic version of the application is written with streamlit. It'll be a lot more flexible if done with js.
