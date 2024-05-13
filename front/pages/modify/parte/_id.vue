<template>
    <v-card class="pa-5">
      <h1 v-if="parte" >Modificar parte: {{ parte.nombre }}</h1>
      <v-form @submit.prevent="actualizarparte" v-if="parte">
        <v-text-field v-model="parte.nombre" label="Nombre" required></v-text-field>
  
        <v-btn type="submit" color="primary">Guardar</v-btn>
      </v-form>
    </v-card>
  </template>
  
  <script>
  export default {
    data() {
      return {
        parte: null
      };
    },
    mounted() {
      this.getparte(this.$route.params.id);
    },
    methods: {
      async getparte(id) {
        try {
          const response = await fetch(`${process.env.API_URL}/partes/${id}`);
          const data = await response.json();
          this.parte = data;
        } catch (error) {
          console.error('Error fetching parte:', error);
        }
      },
      async actualizarparte() {
        try {
          const response = await fetch(`${process.env.API_URL}/partes/${this.parte.id}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.parte)
          });
          if (!response.ok) {
            throw new Error('Error al actualizar el parte');
          }
          this.$router.push(`/partes/${this.parte.id}`);
        } catch (error) {
          console.error('Error al actualizar el parte:', error);
        }
      }
    }
  };
  </script>
  