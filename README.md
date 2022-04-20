# hate-speech-backend

## Installing the Dependencies
1. Clone the repository by using the command `git@github.com:ABCD-EDU/hate-speech-backend.git`
2. Change your current working directory to the repo by using `cd hate-speech-backend`
3. Install dependencies by using `pip install -r requirements.txt`

## Running the server
To run the server on development mode, use the command:
```
python -m uvicorn main:app --reload
```

* Access the server by going to `127.0.0.1:8000`
* Access the documentation by going to `127.0.0.1:8000/docs`

## Folder Structure
```
├───api
│   ├───routes_info
│   └───routes_models
├───bin
│   ├───bert_models
│   ├───json
│   └───svm_models
└───loader
```
### Folder Guide:
### api
This contains the main api package of the backend server. Here you can view the routes by checking the folders with the `routes_` prefic at the beginning.

### bin
This contains all the necessary files for loading the models and information about the project.
1. bert_models - This folder contains the pkl files of the bert model made on the [Hate Speech Model](https://github.com/ABCD-EDU/hate-speech-model) repository.
2. svm_models - This folder contains the pkl files of the SVM model made on the [Hate Speech Model SVM-version](https://github.com/ABCD-EDU/hate-speech-SVM-model)
3. json - This contains the static json files for the project information such as `abstract`, `citation`, `team`, `tags`, `etc`.

### loader
This folder contains the helper tools for loading the saved models and producing the results.