<template>
    <div>
      <v-row>
        <v-col cols="12">
          <v-card-title class="text-h4">Lista de Colores</v-card-title>
        </v-col>
      </v-row>
      <v-container>
        <div v-if="colores.length === 0">No hay colores disponibles</div>
        <v-row v-else>
          <ColorDetalle v-for="(color, index) in colores" :key="index" :color="color" />
        </v-row>
      </v-container>
    </div>
  </template>
  
  <script>
  import ColorDetalle from '@/components/ColorDetalle.vue'; // Asegúrate de tener la ruta correcta hacia el componente
  
  export default {
    components: {
      ColorDetalle,
    },
    data() {
      return {
        colores: [],
      };
    },
    mounted() {
      this.fetchColores();
    },
    methods: {
      async fetchColores() {
        try {
          const response = await fetch(`${process.env.API_URL}/colores`);
          const data = await response.json();
          this.colores = data;
        } catch (error) {
          console.error('Error fetching colores:', error);
        }
      }
    }
  };
  </script>
  