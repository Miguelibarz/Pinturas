<template>
  <v-col cols="6">
    <v-card class="pa-4 d-flex">
      <v-col cols="4" class="color-square pa-2" :style="{ backgroundColor: color?.codigoHex + ' !important' }">
      </v-col>
      <v-col cols="8" class="color-detalle">
        <h2>{{ color.nombre }}</h2>
        <p>ID: {{ color.id }}</p>
        <p>Codigo HEX: {{ color.codigoHex }}</p>
        <p>Marca: {{ color.marca }}</p>

        <v-btn color="red" @click="eliminarColor">Eliminar</v-btn>
      </v-col>
    </v-card>
  </v-col>
</template>

<script>
export default {
  props: {
    color: {
      type: Object,
      required: true
    }
  },
  methods: {
    async eliminarColor() {
      try {
        const response = await fetch(`${process.env.API_URL}/colores/${this.color.id}`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        if (!response.ok) {
          throw new Error('Error al eliminar el color');
        }

        this.$emit('color-eliminado', this.color.id);

        // Recargar la página después de un breve retraso
        setTimeout(() => {
          window.location.reload();
        }, 100);
      } catch (error) {
        console.error('Error al eliminar el color:', error);
      }
    }
  }
};
</script>

<style scoped></style>