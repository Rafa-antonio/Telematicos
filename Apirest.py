const express = require('express');
const app = express();
const books = [
 {
 'id': 1,
 'title': 'La hojarasca',
 'description': 'Bueno',
 'author': 'Gabo'
 },
 {
 'id': 2,
 'title': 'El coronel no tiene quien le escriba',
 'description': 'Interesante',
 'author': 'Gabo'
 }
];

// Obtener todos los libros
// Para probar: curl -i http://localhost:5000/books
app.get('/books', (req, res) => {
 res.json({'books': books});
});

// Obtener un libro por su id
// Para probar: curl -i http://localhost:5000/books/2
app.get('/books/:book_id', (req, res) => {
 const book = books.find(book => book.id === parseInt(req.params.book_id));
 if (!book) {
 res.status(404).send('Libro no encontrado');
 } else {
 res.json({'book': book});
 }
});

// Agregar un nuevo libro
// Para probar: curl -i -H "Content-Type: application/json" -X POST -d '{"title":"El libro"}' http://localhost:5000/books
app.post('/books', (req, res) => {
 if (!req.body.title) {
 res.status(400).send('El título del libro es requerido');
 } else {
 const book = {
 'id': books[books.length - 1].id + 1,
 'title': req.body.title,
 'description': req.body.description || "",
 'author': req.body.author || ""
 };
 books.push(book);
 res.status(201).json({'book': book});
 }
});

// Editar un libro
// Para probar: curl -i -H "Content-Type: application/json" -X PUT -d '{"author":"Jorgito"}' http://localhost:5000/books/2
app.put('/books/:book_id', (req, res) => {
 const book = books.find(book => book.id === parseInt(req.params.book_id));
 if (!book || !req.body) {
 res.status(404).send('Libro no encontrado');
 } else {
 book.title = req.body.title || book.title;
 book.description = req.body.description || book.description;
 book.author = req.body.author || book.author;
 res.json({'book': book});
 }
});

// Eliminar un libro
// Para probar: curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/books/1
app.delete('/books/:book_id', (req, res) => {
 const bookIndex = books.findIndex(book => book.id === parseInt(req.params.book_id));
 if (bookIndex === -1) {
 res.status(404).send('Libro no encontrado');
 } else {
 books.splice(bookIndex, 1);
 res.json({'result': true});
 }
});

app.listen(5000, () => {
 console.log('Servidor en ejecución en el puerto 5000');
});
