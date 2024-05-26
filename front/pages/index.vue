<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6" v-for="button in buttons" :key="button.title">
        <v-card @click="navigate(button.to)" class="pa-5 text-center" hover>
          <v-icon class="mb-4" size="48">{{ button.icon }}</v-icon>
          <v-card-title>{{ button.title }}</v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      buttons: [
        {
          icon: 'mdi-palette-swatch-outline',
          title: 'Modelos',
          to: '/modelos'
        },
        {
          icon: 'mdi-treasure-chest-outline',
          title: 'Partes',
          to: '/partes'
        },
        {
          icon: 'mdi-format-color-fill',
          title: 'Colores',
          to: '/colores'
        },
        {
          icon: 'mdi-palette-outline',
          title: 'Paleta de colores',
          to: '/paleta'
        }
      ]
    };
  },
  methods: {
    navigate(to) {
      this.$router.push(to);
    }
  }
};
</script>

<style scoped>
.v-card {
  cursor: pointer;
  transition: transform 0.3s;
}

.v-card:hover {
  transform: scale(1.05);
}
</style>
