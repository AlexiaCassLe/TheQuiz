# 🧠 The Quiz Game

A small Python-based trivia game where players answer general knowledge questions across different difficulty levels. The goal is to earn points, advance through the levels, and compete for the highest score.

## 🚀 Features

- User registration system  
- Multiple levels: beginner, intermediate, advanced, and pro  
- 3 random questions per level  
- Scores saved in a `.json` file  
- Players can check their current score  
- Questions are loaded from an external file (`preguntas.json`)

## 📂 Project Structure

```
TheQuiz/
├── TheQuiz.py             # Main game script
├── preguntas.json         # File containing all questions by level
├── puntuaciones.json      # Automatically created to store scores
└── README.md              # This file
```

## ▶️ How to Play

1. Make sure Python 3 is installed.
2. Clone the repository or download the files.
3. Run the game:

```bash
python TheQuiz.py
```

4. Register with a username.
5. Answer the questions and earn points.
6. Level up by scoring enough points!

## 📝 Requirements

- Python 3.x

## 💡 Notes

- The `puntuaciones.json` file will be created automatically the first time you play.
- Questions are shuffled every time to avoid repetition.
