<template>
  <v-col cols="6">
    <v-card class="pa-4">
      <router-link :to="'/modelos/' + modelo.id">
        <div style="max-width: 100%; height: auto;">
          <img v-if="modelo && modelo.imagen" :src="`/images/${modelo.imagen}`"
            style="width: 100%;">
        </div>
        <div class="modelo-detalle">
          <h2>{{ modelo.nombre }}</h2>
          <p>Resumen: {{ modelo.resumen }}</p>
          <p>Creador:
            <router-link :to="'/users/' + creador.id">
              {{ creador.alias }}
            </router-link>
          </p>
        </div>
      </router-link>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    modelo: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      creador: {},
      error: ''
    };
  },
  watch: {
    'modelo.idUser': {
      immediate: true, // Llama a fetchCreador() inmediatamente después de la creación del componente
      handler(newVal) {
        if (newVal) {
          this.fetchCreador();
        }
      }
    }
  },
  methods: {
    async fetchCreador() {
      try {
        const response = await fetch(`${process.env.API_URL}/users/${this.modelo.idUser}`);
        const data = await response.json();
        this.creador = data;
      } catch (error) {
        console.error('Error fetching creador:', error);
        this.error = 'Error al obtener el creador del modelo.';
      }
    }
  }
};
</script>

<style scoped></style>
