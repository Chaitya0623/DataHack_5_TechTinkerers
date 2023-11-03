# ResuGenius
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/7394a454-6789-4810-a180-17578683a811)

* The product can initially take in input in the form of uploading a file (any type), video resume and a fueler profile too. The model then extracts the best skills of the user by using the MNLI model to perform **zero shot classification** and give the probability of the user's strongest tech stacks. The projects obtained are validated by checking them with their corresponding GitHub links extracted via Web Scraping.
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/fc3d84bb-f06f-4650-a0b8-7d8fbf4cfd08)

* There is another page where users can put in their projects, validate them, and create a custom project portfolio.
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/b8c6a833-6d9e-49b9-bd1f-829225082507)
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/7ef7307a-dbd1-4fdb-9fb8-5d520cca0bdd)

* Depending on the projects that the user has already worked on, the job descriptions are matched via semantic similarity using the **FAISS** vector store.
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/71f8484c-f954-4a49-bb57-0f2fc5e19082)

* Depending on the strengths and weakness of the user, teammates are recommended, ensuring collaborative development.
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/5688ff41-0a74-4fe0-8ba4-0bda53dd886b)

* Depending on the current skills extracted, projects are recommended to the user, not only to learn new stacks, but also to garnish the already good skills.
![image](https://github.com/Chaitya0623/DataHack_5_TechTinkerers/assets/91510927/73304af0-dd5d-42d9-82cf-7f51da6269cf)

* The project also focusses on extracting the confidence of the user based on his **video resume**, showing his readiness for non technical roles.
* **Multilingual Resumes** can be fed in the model, it will translate it into english and follow the same steps as mentioned above.
