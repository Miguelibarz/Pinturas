<template>
  <v-card class="pa-5">
    <v-row>
      <v-col cols="2">
        <v-card style="max-width: 100%; height: auto;" class="rounded-lg">
          <img v-if="modelo && modelo.imagen" :src="`/images/${modelo.imagen}`" alt="Imagen del modelo"
            style="width: 100%;">
        </v-card>
      </v-col>
      <v-col cols="7" class="align-center d-flex">
        <v-card-title v-if="modelo" class="text-h2 pa-4">{{ capitalize(modelo.nombre) }} </v-card-title>
      </v-col>

      <v-col cols="3" class="d-flex justify-end align-center pa-6" v-if="modelo">
        <v-btn :to="'/Modelos'" color="primary"> <v-icon>mdi-arrow-left</v-icon></v-btn>
        <v-btn class="ma-1" :to="`../Add/parte/${modelo.id}`">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
        <v-btn class="ma-1" :to="`../modify/modelo/${modelo.id}`" color="info">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn class="ma-1" @click="deleteCurrentModel" color="error">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-divider class="border-opacity-75 pa-4"></v-divider>

    <v-card-text class="pa-4" v-if="modelo">
      {{ capitalize(modelo.resumen) }}
    </v-card-text>
    <v-divider class="border-opacity-75 pa-4"></v-divider>
    <v-card-text class="pa-4 text-h5">Partes:</v-card-text>
    <v-container class="d-flex">
      <TarjetaParte v-for="(parte, index) in partes" :key="index" :parte="parte" />
    </v-container>
  </v-card>
</template>

<script>
import TarjetaParte from '~/components/TarjetaParte.vue';

export default {
  components: {
    TarjetaParte
  },
  data() {
    return {
      modelo: null,
      partes: []
    };
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler(newValue) {
        this.getModelo(newValue);
      }
    }
  },
  mounted() {
    this.getModelo(this.$route.params.id);
  },
  methods: {
    capitalize(string) {
      return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    },
    async getModelo(id) {
      try {
        // Fetch model details
        const responseModelo = await fetch(process.env.API_URL + `/modelos/${id}`);
        const dataModelo = await responseModelo.json();
        this.modelo = dataModelo;

        // Fetch associated partes
        const responsePartes = await fetch(process.env.API_URL + `/getPartes/${id}`);
        const dataPartes = await responsePartes.json();
        this.partes = dataPartes;
      } catch (error) {
        console.error('Error fetching modelo:', error);
      }
    },
    async deleteCurrentModel() {
      try {
        await fetch(`${process.env.API_URL}/modelos/${this.modelo.id}`, {
          method: 'DELETE',
        });
        // Redirigir a /modelos
        this.$router.push('/modelos');
      } catch (error) {
        console.error('Error al eliminar el modelo:', error);
      }
    }
  }
};
</script>