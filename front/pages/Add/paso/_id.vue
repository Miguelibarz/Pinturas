<template>
  <v-card class="pa-4">
    <h1>Crear Nuevo Paso</h1>
    <v-form @submit.prevent="crearPaso">
      <v-text-field v-model="nombre" label="Nombre" required></v-text-field>
      <v-select v-model="Color" :items="colores" item-text="nombre" label="Color" return-object
        :search-input.sync="search" dense>
        <template v-slot:item="{ item }">
          <span>{{ item.nombre }}</span>
        </template>
      </v-select>
      <v-col cols="1" class="color-square pa-2" :style="{ backgroundColor: Color?.codigoHex + ' !important' }"></v-col>
      <v-text-field v-model="comentario" label="Comentario"></v-text-field>
      <v-btn type="submit" color="info">Guardar</v-btn>
      <v-btn @click="navigateToPartes" color="error">Cancelar</v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      nombre: '',
      Color: null,
      comentario: '',
      colores: [],
      search: '' // Modelo para la búsqueda
    };
  },
  mounted() {
    this.fetchColores();
  },
  methods: {
    navigateToPartes() {
      if (this.$route) {
        this.$router.push(`/partes/${this.$route.params.id}`);
      } else {
        console.error('Route is not available');
      }
    },
    async fetchColores() {
      try {
        const response = await fetch(process.env.API_URL + '/colores');
        const data = await response.json();
        this.colores = data;
      } catch (error) {
        console.error('Error fetching colores:', error);
      }
    },
    async crearPaso() {
      const requestBody = {
        nombre: this.nombre,
        idColor: this.Color.id,
        idParte: this.$route.params.id,
        comentario: this.comentario
      };

      try {
        const response = await fetch(process.env.API_URL + '/pasos', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestBody)
        });
        this.$router.push(`/partes/${this.$route.params.id}`);

        if (!response.ok) {
          throw new Error('Error al crear el paso');
        }
      } catch (error) {
        console.error('Error al crear el paso:', error);
      }
    }
  }
};

</script>
