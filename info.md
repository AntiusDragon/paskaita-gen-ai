# Komandos sukuriant nauja projekta:
### sukuria pradinius failus
```sh
uv init
```
### sukuriam ".gitignore"
### venv dažniausiai naudojamas duomenu biblioteka
```sh
uv venv
```
### turim aktivuoti venv su komanda
```sh
.venv\Scripts\activate
```
### tada tesem terminalo kodus
```sh
uv add openai
```
### naudojam ši komanda kad suprastu ".evn" faila
```sh
uv add python-dotenv
```
### Pastaba turi buti trumpas GIT_KEY raktas
```sh
turi veikti
```
### pridedam dar "rich"
```sh
uv add rich
```
```sh
uv add streamlit
```
```sh
streamlit run main.py
```



### naudojam test koda
```sh
python main.py
```
### rei norim pašalinti openai
```sh
uv remove openai
```
### jei nera aplankalo ".venv" tada insrašom ši komanda kad inrašitu priedus
```sh
uv sync
```
### kai inrašo priedus turim ji pajungti su šio kodu
```sh
.venv\Scripts\activate
```
