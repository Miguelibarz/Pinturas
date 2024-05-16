<template>
  <v-card class="pa-4">
    <h1>Crear Nuevo Modelo</h1>
    <v-form @submit.prevent="crearModelo">
      <v-text-field v-model="nombre" label="Nombre" required></v-text-field>
      <v-text-field v-model="imprimacion" label="Imprimación"></v-text-field>
      <v-checkbox v-model="visibilidad" label="Visible"></v-checkbox>
      <v-textarea v-model="resumen" label="Resumen"></v-textarea>
      <input type="file" ref="fileInput" @change="handleFileChange" accept="image/*" />
      <v-btn type="submit" color="primary">Guardar</v-btn>
    </v-form>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      nombre: '',
      imprimacion: '',
      visibilidad: true,
      resumen: '',
      imagen: '',
      file: null,
    }
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
      const currentDate = new Date();
      //crea nombre unico con el nombre de la imagen y la fecha
      this.imagen = currentDate.getTime() + "-" + this.file.name;
    },
    crearModelo() {
      const requestBody = {
        nombre: this.nombre,
        imprimacion: this.imprimacion,
        visibilidad: this.visibilidad,
        resumen: this.resumen,
        idUser: 1,
        imagen: this.imagen
      };

      fetch(process.env.API_URL + '/modelos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody)

      }).then(response => {
        if (!response.ok) {
          throw new Error('Error al crear el modelo');
        }
        else {
          this.guardarImagen(this.file, this.imagen)
        };
        this.$router.push('/modelos');
      }).catch(error => {
        console.error(error);
      });
    },
    async guardarImagen(file, name) {
      const formData = new FormData();
      formData.append('file', file, name);

      try {
        const response = await fetch(process.env.API_URL + '/upload', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          throw new Error('Error al subir la imagen');
        }

        const data = await response.json();
      } catch (error) {
        console.error(error.message);
      }
    }
  }
}
</script>
