<template>
    <v-card class="pa-4">
        <h1>Crear Nueva parte</h1>
        <v-form @submit.prevent="crearParte">
            <v-text-field v-model="nombre" label="Nombre" required></v-text-field>
            <input type="file" ref="fileInput" @change="handleFileChange" accept="image/*" />
            <v-divider class="py-2" />
            <v-btn type="submit" color="primary">Guardar</v-btn>
            <v-btn @click="navigateToModel" color="error">Cancelar</v-btn>

        </v-form>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            nombre: '',
            idModelo: null,
            file: null,
        }
    },
    mounted() {
        // Obtener la ID del modelo de la URL y asignarla a la variable
        this.idModelo = this.$route.params.id;
    },
    methods: {
        handleFileChange(event) {
            this.file = event.target.files[0];
            const currentDate = new Date();
            //crea nombre unico con el nombre de la imagen y la fecha
            this.imagen = currentDate.getTime() + "-" + this.file.name;
            console.log(this.imagen);
        },
        navigateToModel() {
            if (this.$route) {
                this.$router.push(`/modelos/${this.$route.params.id}`);
            } else {
                console.error('Route is not available');
            }
        },
        crearParte() {
            const requestBody = {
                nombre: this.nombre,
                idModelo: this.idModelo,
                imagen: this.imagen
            };

            fetch(process.env.API_URL + '/partes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody)
            }).then(response => {
                if (!response.ok) {
                    throw new Error('Error al crear la parte');
                }
                else {
                    this.guardarImagen(this.file, this.imagen)
                    console.log("Parte creada");
                };
                // Redirigir a /Partes
                this.$router.push(`/modelos/${this.idModelo}`);
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
