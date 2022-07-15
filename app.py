import streamlit as st
import random

st.set_page_config(page_title="PyconPrizes", layout="wide")
random_seed = st.sidebar.number_input("Random Seed", value=0, min_value=0, max_value=100)
random.seed(random_seed)

st.title("PyDay - Repartiendo los premios")
c1, c2 = st.columns(2)

personas = [
"Riva",
"Stephanie",
"Cristina", 
"Kalfu", 
"Mauricio", 
"Alonso", 
"Jorge", 
"Benjamin", 
"Nicole", 
"Alejandro",
"Alberto", 
"Francisco", 
"Sebastian"
]

c1.markdown( "* " + "\n* ".join(personas))

premios_dict = {
    "Cursos Levagon":3,
    "Jetbrain":1,
    "Github":2,
    "Libros Python Tricks":2,
    "Libros Python Basics":2,
     }

premios_list = []
for key, value in premios_dict.items():
    premios_list += [key] * value

with c2:
    c2.markdown( "* " + "\n* ".join(premios_list))

shuffled_people = personas.copy()
random.shuffle(shuffled_people)

shuffled_prizes = premios_list.copy()
random.shuffle(shuffled_prizes)

st.title("Premios repartidos")

if "i" not in st.session_state:
    st.session_state["i"] = 0

if "shown_prizes" not in st.session_state:
    st.session_state["shown_prizes"] = ""

if st.button("Ver premio"):
    c1, c2 = st.columns([2, 1])
    if st.session_state["i"] < len(shuffled_prizes):
        i = st.session_state.i
        persona = shuffled_people[i]
        premio = shuffled_prizes[i]
        text = f" {persona} ganó el premio #{i}: {premio}"
        c1.title(text)
        st.balloons()
        st.session_state["i"] += 1
        st.session_state["shown_prizes"] += "* "+ text + "\n"
        #st.markdown(st.session_state["shown_prizes"])
    else:
        loosers = shuffled_people[len(shuffled_prizes):]
        loosers_mkd = '* ' + "\n* ".join(loosers)
        st.warning("No hay más premios")
        c1, c2, c3, c4 = st.columns([2, 1, 2, 1])
        c1.write("### Ganadores")
        c1.markdown(st.session_state["shown_prizes"])
        c2.write("")
        c2.write("")
        c2.write("")
        c2.write("")
        c2.write("")
        c2.image("cat.gif")
        c3.write("### Siga participando")
        c3.markdown(loosers_mkd)
        c4.image("https://img-9gag-fun.9cache.com/photo/amg5Ebj_460s.jpg")

else:
    st.error("Apreta el boton, poh!")
