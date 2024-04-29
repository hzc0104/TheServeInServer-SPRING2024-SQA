# The Serve In Server Reports
### Forensics Screenshot/Log
![Screenshot 2024-04-29 094006](https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/9271f264-ed77-4b89-b9f3-d52ccc2d7d89)

![image](https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/d49d4d60-c21c-45ee-9781-2419b08afd7d)

![image](https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/c91ef710-10a4-4c10-8ddf-522f64821285)

Note: This file will use the logger function to log all of the activity and while running the forensics. The log will be produced once the program is done running. 

### Fuzzing Screenshot/Log
<img width="1045" alt="Screenshot 2024-04-28 at 10 46 38 PM" src="https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/e70c8f78-4c86-4ffa-987e-453e6665a820">

### Static Analysis Screenshot/Log
<img width="1052" alt="Screenshot 2024-04-26 at 11 42 00 AM" src="https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/aefcff39-3319-4c6c-82d2-fdf385fb74c3">
<img width="1051" alt="Screenshot 2024-04-26 at 11 42 15 AM" src="https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/f9e72d55-b58e-4b73-8726-ec3a430ceb72">
<img width="1049" alt="Screenshot 2024-04-26 at 11 42 40 AM" src="https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/6ffa621b-5493-46c9-b3a0-cc5b6373f3f8">

### Pre-Commit file Screenshot
<img width="658" alt="Screenshot 2024-04-28 at 11 02 47 PM" src="https://github.com/hzc0104/TheServeInServer-SPRING2024-SQA/assets/164685184/874e8bfb-858a-4796-b703-6c7f42b41ffb">

### Report
Our knowledge came from the collection of each other and the given workshops throughout the semester. First we unzippped the file, we created a file within .git/hooks/pre-commit to run a scan on all security weaknesses using the code: bandit . -r, creating a fuzz.py file, integrating forensics, with continous integration into github. 

