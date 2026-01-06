<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

// Variables reactivas
const characters = ref([])
const search = ref('')
const loading = ref(false)

// Función para pedir datos a TU Backend (Python)
const fetchCharacters = async () => {
  loading.value = true
  try {
    // Petición al endpoint que creamos hace rato
    const response = await axios.get('http://127.0.0.1:5000/api/characters', {
      params: { search: search.value } // Enviamos lo que escribas en el buscador
    })
    characters.value = response.data.characters
  } catch (error) {
    console.error("Error conectando con el servidor:", error)
  } finally {
    loading.value = false
  }
}

// Watcher: Detecta cuando escribes y busca automáticamente
watch(search, () => {
  fetchCharacters()
})

// Cargar personajes al abrir la página
onMounted(fetchCharacters)
</script>

<template>
  <div class="container">
    <header>
      <h1>Star Wars Database</h1>
      <input 
        v-model="search" 
        type="text" 
        placeholder="Buscar personaje (ej. Luke)..." 
        class="search-input"
      />
    </header>

    <main>
      <div v-if="loading" class="loading">Cargando la fuerza...</div>
      
      <div v-else class="grid">
        <div v-for="char in characters" :key="char.id" class="card">
          <div class="card-image">
            <img :src="char.image_url" :alt="char.name" />
          </div>
          <div class="card-info">
            <h3>{{ char.name }}</h3>
          </div>
        </div>
      </div>

      <div v-if="!loading && characters.length === 0" class="no-results">
        No se encontraron personajes.
      </div>
    </main>
  </div>
</template>

<style scoped>
/* Estilos oscuros tipo Star Wars */
.container { max-width: 1000px; margin: 0 auto; padding: 40px; font-family: sans-serif; color: #fff; }
header { text-align: center; margin-bottom: 50px; }
h1 { color: #FFE81F; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 2px; }

.search-input {
  width: 100%; max-width: 400px; padding: 15px; border-radius: 25px;
  border: 2px solid #FFE81F; background: #222; color: #fff; font-size: 1.1rem; outline: none;
}

.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 30px; }
.card { background: #1a1a1a; border-radius: 15px; overflow: hidden; transition: transform 0.3s, box-shadow 0.3s; border: 1px solid #333; }
.card:hover { transform: translateY(-5px); box-shadow: 0 0 15px rgba(255, 232, 31, 0.3); border-color: #FFE81F; }

.card-image { height: 280px; width: 100%; }
.card-image img { width: 100%; height: 100%; object-fit: cover; }
.card-info { padding: 15px; text-align: center; }
.card-info h3 { margin: 0; font-weight: normal; letter-spacing: 1px; }

.loading, .no-results { text-align: center; font-size: 1.5rem; color: #888; margin-top: 50px; }
</style>