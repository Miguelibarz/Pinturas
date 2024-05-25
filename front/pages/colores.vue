<template>
  <div>
    <v-row>
      <v-col cols="10">
        <v-card-title class="text-h4">Lista de colores</v-card-title>
      </v-col>
      <v-col cols="2" class="d-flex justify-end align-center pa-6">
        <v-btn @click="importColores">
          <v-icon>mdi-plus</v-icon>
           Importar desde fichero
        </v-btn>
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
import ColorDetalle from '@/components/ColorDetalle.vue'; 

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
    },
    async importColores() {
      try {
        const response = await fetch(`${process.env.API_URL}/import-colores/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
        });
        const data = await response.json();
        this.colores = data;
      } catch (error) {
        console.error('Error importing colores:', error);
      }
    }
    
  }
};
</script>