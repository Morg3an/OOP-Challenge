# 🐾 Virtual Pet Challenge – Python OOP Project

Welcome to the **Python OOP Challenge**! 🎉  
In this challenge, you'll create and interact with your very own virtual pet using **Object-Oriented Programming** concepts in Python. It's a great way to strengthen your understanding of classes, attributes, and methods while having some fun!

---

## 📚 Challenge Objective

Create a `Pet` class with the following:

### 🔧 Attributes
- `name`: Name of your pet
- `hunger`: Integer (0 = full, 10 = very hungry)
- `energy`: Integer (0 = tired, 10 = fully rested)
- `happiness`: Integer (0–10)
- `tricks`: List of tricks the pet has learned (Bonus)

### 🧠 Methods
- `eat()`: Decrease hunger by 3 (min 0), increase happiness by 1 (max 10)
- `sleep()`: Increase energy by 5 (max 10)
- `play()`: Decrease energy by 2, increase happiness by 2, and increase hunger by 1
- `get_status()`: Print current state of the pet
- `train(trick)`: Teach a new trick (Bonus)
- `show_tricks()`: Display all learned tricks (Bonus)

Use `max()` and `min()` to ensure attributes stay between 0 and 10.

---

## 🚀 How to Run the Program

### 1. Clone the Repository or Download ZIP
```bash
git clone https://github.com/Morg3an/OOP-Challenge.git
```

Or download the `.zip` and extract it.

## 2. Run the Program

Make sure you have Python 3 installed. Then run:

```bash
cd OOP-Challenge
python main.py
```

### 📂 Project Structure
```bash
OOP-Challenge/
│
├── pet.py          # Contains the Pet class and logic
├── main.py         # Run and interact with your pet here
└── README.md       # This file!
```

### ✅ Sample Output
```bash
Creating pet: Max
Max is eating...
Max is playing...
Max is sleeping...
Max is learning a new trick: roll over!
Max is learning a new trick: play dead!

Max's current status:
Hunger: 2
Energy: 8
Happiness: 9
Tricks: ['roll over', 'play dead']

Max knows the following tricks: roll over, play dead
```