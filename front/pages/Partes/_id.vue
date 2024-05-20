<template>
  <v-card class="pa-5">
    <v-row>
      <v-col cols="2">
        <v-card style="max-width: 100%; height: auto;" class="rounded-lg">
          <img v-if="parte && parte.imagen" :src="`/images/${parte.imagen}`"
            style="width: 100%;">
        </v-card>
      </v-col>
      <v-col cols="7" class="align-center d-flex">
        <v-card-title v-if="parte" class="text-h2 pa-4">{{ capitalize(parte.nombre) }}</v-card-title>
      </v-col>
      <v-col cols="3" class="d-flex justify-end align-center pa-6">
        <v-btn class="ma-1" v-if="parte" :to="`../Add/paso/${parte.id}`">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
        <v-btn class="ma-1" v-if="parte" :to="`../modify/parte/${parte.id}`" color="info">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn class="ma-1" @click="deleteCurrentParte" color="error">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-divider class="border-opacity-75 pa-4" ></v-divider>
    <PasosDetalle v-for="(pasos, index) in pasos" :key="index" :pasos="pasos" />
  </v-card>
</template>

<script>
import PasosDetalle from '~/components/PasosDetalle.vue';

export default {
  data() {
    return {
      parte: null,
      pasos: []
    };
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler(newValue) {
        this.getParte(newValue);
      }
    }
  },
  mounted() {
    this.getParte(this.$route.params.id);
  },
  methods: {
    capitalize(string) {
      return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    },
    async getParte(id) {
      try {
        // Fetch partes details
        const responseParte = await fetch(process.env.API_URL + `/partes/${id}`);
        const dataParte = await responseParte.json();
        this.parte = dataParte;
        // Fetch associated pasos
        const responsePasos = await fetch(process.env.API_URL + `/getPasos/${id}`);
        const dataPasos = await responsePasos.json();
        this.pasos = dataPasos;
      } catch (error) {
        console.error('Error fetching pasos:', error);
      }
    },
    async deleteCurrentParte() {
      try {
        await fetch(`${process.env.API_URL}/partes/${this.parte.id}`, {
          method: 'DELETE',
        });
        // Redirigir a /partes
        this.$router.push('/modelos');
       } catch (error) {
        console.error('Error al eliminar el parte:', error);
      }
    }
  }
};
</script>
