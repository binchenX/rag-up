# run ollama
❯❯ docker run -d -v $(PWD)/data:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# comment to ollama container
❯❯ docker exec -it ollama bash

# run llm
# this will download the llm image and run it, if llm image already exists it will start the llm image
root@c96f4fc1be6f:/# ollama run phi
>>>

# ask question
root@c96f4fc1be6f:/# ollama run phi
>>> what is docker
 Docker is a platform for building,

# exit
>>> /bye
root@c96f4fc1be6f:/#

# reconnect
root@c96f4fc1be6f:/# ollama run phi
>>>

# ask question via curl
# stream true will send work one by one as stream
❯❯ curl http://localhost:11434/api/generate -d '{
  "model": "phi",
  "prompt": "Why is docker?",
  "stream": true
}'
{"model":"phi","created_at":"2024-03-16T23:41:47.08021936Z","response":" Docker","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.171298057Z","response":" is","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.229011776Z","response":" a","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.287024996Z","response":" platform","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.34490784Z","response":" that","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.402687143Z","response":" allows","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.461930866Z","response":" users","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.520328713Z","response":" to","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.578350933Z","response":" create","done":false}
{"model":"phi","created_at":"2024-03-16T23:41:47.636073277Z","response":",","done":false}

# ask question without stream
# wail till getting full response from llm and output, will take considerabile time
❯❯ curl http://localhost:11434/api/generate -d '{
  "model": "phi",
  "prompt": "Why is docker?",
  "stream": false
}'
{"model":"phi","created_at":"2024-03-16T23:42:34.140800795Z","response":" Docker is a containerization platform that allows you to package your application code, dependencies, and runtime environment into a single executable container. This makes it easy to run your applications on any machine with Docker installed, as long as the container has the necessary dependencies and configuration settings. Containers are also more isolated from each other than traditional installations of applications, which can help improve performance and security. Additionally, Docker provides tools for automating common tasks such as building and deploying containers, making it a popular choice among developers and IT professionals.\n","done":true,"context":[11964,25,317,8537,1022,257,11040,2836,290,281,11666,4430,8796,13,383,8796,3607,7613,7429,284,262,2836,338,2683,13,198,12982,25,4162,318,36253,30,198,48902,25,25716,318,257,9290,1634,3859,326,3578,345,284,5301,534,3586,2438,11,20086,11,290,19124,2858,656,257,2060,28883,9290,13,770,1838,340,2562,284,1057,534,5479,319,597,4572,351,25716,6589,11,355,890,355,262,9290,468,262,3306,20086,290,8398,6460,13,2345,50221,389,635,517,11557,422,1123,584,621,4569,26162,286,5479,11,543,460,1037,2987,2854,290,2324,13,12032,11,25716,3769,4899,329,3557,803,2219,8861,884,355,2615,290,29682,16472,11,1642,340,257,2968,3572,1871,6505,290,7283,11153,13,198],"total_duration":6343449574,"load_duration":21148773,"prompt_eval_duration":65335000,"eval_count":107,"eval_duration":6256397000}%
