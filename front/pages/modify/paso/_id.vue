<template>
  <v-card class="pa-5">
    <h1 v-if="paso">Modificar paso: {{ paso.nombre }}</h1>
    <v-form @submit.prevent="actualizarpaso" v-if="paso">
      <v-text-field v-model="paso.nombre" label="Nombre" required></v-text-field>
      <v-select v-model="Color" :items="colores" item-text="nombre" label="Color" return-object
        :search-input.sync="search" dense />
      <v-textarea v-model="paso.comentario" label="Resumen"></v-textarea>
      <v-btn type="submit" color="primary">Guardar</v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      paso: null,
      colores: [],
      Color: null, // Add Color where id = idColor
      search: '' // Modelo para la búsqueda
    };
  },
  mounted() {
    this.fetchColores().then(() => {
      this.getpaso(this.$route.params.id);
    });
  },
  methods: {
    async fetchColores() {
      try {
        const response = await fetch(process.env.API_URL + '/colores');
        const data = await response.json();
        this.colores = data;
      } catch (error) {
        console.error('Error fetching colores:', error);
      }
    },
    async getpaso(id) {
      try {
        const response = await fetch(`${process.env.API_URL}/pasos/${id}`);
        const data = await response.json();
        this.paso = data;

        // Acceder a this.colores en lugar de colores
        this.Color = this.colores.find(color => color.id == this.paso.idColor);

      } catch (error) {
        console.error('Error fetching paso:', error);
      }
    },
    async actualizarpaso() {
      try {
        // Extraer solo la ID del color seleccionado
        const colorId = this.Color.id;

        // Actualizar el paso con la ID del color seleccionado
        this.paso.idColor = colorId;

        // Eliminar el objeto completo del paso antes de enviar la solicitud PUT
        const { color, ...pasoData } = this.paso;

        const response = await fetch(`${process.env.API_URL}/pasos/${pasoData.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(pasoData)
        });

        if (!response.ok) {
          throw new Error('Error al actualizar el paso');
        }

        this.$router.push(`/partes/${this.paso.idParte}`);
      } catch (error) {
        console.error('Error al actualizar el paso:', error);
      }
    }

  }
};
</script>