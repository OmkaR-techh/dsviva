const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// 🔥 Connect to MongoDB
mongoose.connect("mongodb+srv://OMKARS:OMKAR2006@cluster0.5jthsd5.mongodb.net/myproject")
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

// Create Schema
const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    age: Number
});

// Create Model
const User = mongoose.model("User", userSchema);

// Save Route
app.post('/save', async (req, res) => {
    try {
        const newUser = new User(req.body);
        await newUser.save();
        res.json({ message: "Data saved to MongoDB!" });
    } catch (error) {
        res.status(500).json({ message: "Error saving data" });
    }
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});