require('dotenv').config();

const express = require('express');
const cors = require('cors');
const logRoutes = require('./routes/logRoutes');

const app = express();

app.use(cors());
app.use(express.json());

app.use('/api', logRoutes);

const PORT = process.env.PORT;

app.listen(PORT, () => {
    console.log(`Serviço rodando na porta ${PORT}`);
});