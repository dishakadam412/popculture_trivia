import streamlit as st

# ------------------------------
# Backend Data
# ------------------------------
questions = [
    "What is the name of Elvis Presley's Memphis home?:",
    "Before embarking on a solo career, Beyoncé was part of what R&B group?:",
    "Breaking Bad actor Bryan Cranston won a Tony Award for his performance in what 2014 Broadway play?:",
    "In what fictional Indiana town does the sci-fi series Stranger Things take place?:",
    "What was Taylor Swift's first song to chart on the Billboard Hot 100?:"
]

options = [
    ("A. Graceland", "B. Brown", "C. Junior", "D. Grayson"),
    ("A. Jagged Edge", "B. TLC", "C. Destiny's Child", "D. The Supremes"),
    ("A. Aladdin", "B. A Raisin in the Sun", "C. All the Way", "D. Act One"),
    ("A. Heggins", "B. Hawkins", "C. Munster", "D. Camel"),
    ("A. Tim McGraw", "B. Love Story",
     "C. You Belong With Me", "D. I Knew You Were Trouble")
]

answers = ["A", "C", "C", "B", "A"]

# ------------------------------
# Initialize Session State
# ------------------------------
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'guesses' not in st.session_state:
    st.session_state.guesses = []

# ------------------------------
# Streamlit Layout
# ------------------------------
st.title("🎤 Pop Culture Quiz Game")
st.write("Answer the questions below! Select the correct option.")

if st.session_state.q_index < len(questions):
    q_num = st.session_state.q_index
    st.subheader(f"Q{q_num + 1}: {questions[q_num]}")

    # Display options as buttons
    cols = st.columns(4)
    for i, option in enumerate(options[q_num]):
        if cols[i].button(option) and not st.session_state.answered:
            st.session_state.guesses.append(option[0])  # store the letter
            st.session_state.answered = True
            if option[0] == answers[q_num]:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! Correct answer: {answers[q_num]}")

    st.progress((q_num + 1) / len(questions))
    st.write(f"Score: {st.session_state.score}/{len(questions)}")

    # Next question button
    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.q_index += 1
            st.session_state.answered = False

# Quiz completed
else:
    st.balloons()
    st.success(
        f"🎉 Quiz Completed! Final Score: {st.session_state.score}/{len(questions)}")
    st.write("### Correct Answers: ", ", ".join(answers))
    st.write("### Your Guesses: ", ", ".join(st.session_state.guesses))

    # Reset quiz
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.answered = False
        st.session_state.guesses = []
