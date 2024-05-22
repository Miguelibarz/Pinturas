<template>
  <v-col cols="6">
    <v-card class="pa-4 tarjeta-modelos">

      <router-link :to="'/modelos/' + modelo.id" class="enlace">
        <div style="max-width: 100%; height: auto;">
          <img v-if="modelo && modelo.imagen" :src="`/images/${modelo.imagen}`" style="width: 100%;">
        </div>
        <div class="modelo-detalle">
          <h2>{{ capitalizeFirst(modelo.nombre) }}</h2>
          <p>Resumen: {{ capitalizeFirst(modelo.resumen) }}</p>
          <p>Creador:
              <!--<router-link :to="'/users/' + creador.id">-->
                {{ creador.alias }}
              <!--</router-link>-->
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
    },
    capitalizeFirst(text) {
      if (!text) return '';
      return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    }
  }
};
</script>

<style scoped>
.enlace {
  text-decoration: none;
  color: #fff
}

.enlace:hover {
  color: #dadada
}

.tarjeta-modelos:hover {
  background-color: #dadada;
  transform: scale(1.05);
}

.tarjeta-modelos {
  transition: transform 0.3s ease;
}
</style>
