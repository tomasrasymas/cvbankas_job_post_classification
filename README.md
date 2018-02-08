# cvbankas_job_post_classification
Automatic cvbankas.lt web site job post classification into categories.

Job post categories:
* Administravimas/sekretoriavimas
* Apsauga
* Apskaita/finansai/auditas
* Dizainas/architektūra
* Draudimas
* Eksportas
* Energetika/elektronika
* Informacinės technologijos
* Inžinerija/mechanika
* Klientų aptarnavimas/paslaugos
* Maisto gamyba
* Marketingas/reklama
* Medicina/sveikatos apsauga/farmacija
* Nekilnojamasis turtas
* Pardavimų vadyba
* Personalo valdymas
* Pirkimai/tiekimas
* Pramonė/gamyba
* Prekyba - konsultavimas
* Sandėliavimas
* Statyba
* Teisė
* Transporto vairavimas
* Transporto/logistikos vadyba
* Vadovavimas/valdymas
* Valstybės tarnyba
* Švietimas/mokymai/kultūra
* Žemės ūkis/žuvininkystė
* Žiniasklaida/viešieji ryšiai

### Pipeline used
1. Scrape web site for job posts.
2. Remove stop words and punctuation from text.
3. CountVectorizer
4. TfidfTransformer
5. Job post text classification using: MultinomialNB / RandomForestClassifier / DecisionTreeClassifier / KNeighborsClassifier / DNN

### Results
1. MultinomialNB classifier - 0.6876370013152127
2. RandomForest classifier - 0.68478737395879
3. DecisionTree classifier - 0.5594037702761947
4. KNeighbors classifier - 0.6900482244629549
5. Keras Sequential model - 0.74


Classification models accuracy achieved is too low to use in production environment. Steps to try to improve classification accuracy:
1. Gather more training data (data set used in this experiment to too small).
2. Try to use PCA for features dimension reduction.
3. Try to use features scaling.
4. Experiment with different hyperparameters (automatic hyperparameter tuning software like Auto-WEKA, TPOT, etc.).