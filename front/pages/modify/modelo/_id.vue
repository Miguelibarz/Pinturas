<template>
  <v-card class="pa-5">
    <h1 v-if="modelo" >Modificar Modelo: {{ modelo.nombre }}</h1>
    <v-form @submit.prevent="actualizarModelo" v-if="modelo">
      <v-text-field v-model="modelo.nombre" label="Nombre" required></v-text-field>
      <v-text-field v-model="modelo.imprimacion" label="Imprimación"></v-text-field>
      <v-checkbox v-model="modelo.visibilidad" label="Visibilidad"></v-checkbox>
      <v-textarea v-model="modelo.resumen" label="Resumen"></v-textarea>
      
      <!-- Agrega más campos según sea necesario -->

      <v-btn type="submit" color="primary">Guardar</v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      modelo: null
    };
  },
  mounted() {
    this.getModelo(this.$route.params.id);
  },
  methods: {
    async getModelo(id) {
      try {
        const response = await fetch(`${process.env.API_URL}/modelos/${id}`);
        const data = await response.json();
        this.modelo = data;
      } catch (error) {
        console.error('Error fetching modelo:', error);
      }
    },
    async actualizarModelo() {
      try {
        const response = await fetch(`${process.env.API_URL}/modelos/${this.modelo.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.modelo)
        });
        if (!response.ok) {
          throw new Error('Error al actualizar el modelo');
        }
        this.$router.push(`/modelos/${this.modelo.id}`);
      } catch (error) {
        console.error('Error al actualizar el modelo:', error);
      }
    }
  }
};
</script>
