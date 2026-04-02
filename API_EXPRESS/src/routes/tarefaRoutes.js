const express = require('express');
const router = express.Router();
const TarefaController = require('../controllers/TarefaController');

// O "Guarda-costas"
const authMiddleware = require('../middlewares/authMiddleware');

// Todas as rotas abaixo passam pelo authMiddleware antes de chegar no Controller
router.post('/', authMiddleware, TarefaController.criar);
router.get('/', authMiddleware, TarefaController.listar);
router.patch('/:id', authMiddleware, TarefaController.alterarStatus); // PATCH é usado para atualizações parciais

module.exports = router;