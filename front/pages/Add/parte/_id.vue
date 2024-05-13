<template>
    <v-card class="pa-4">
        <h1>Crear Nueva parte</h1>
        <v-form @submit.prevent="crearParte">
            <v-text-field v-model="nombre" label="Nombre" required></v-text-field>
            <v-btn type="submit" color="primary">Guardar</v-btn>
        </v-form>
    </v-card>
</template>

<script>
export default {
    data() {
        return {
            nombre: '',
            idModelo: null
        }
    },
    mounted() {
        // Obtener la ID del modelo de la URL y asignarla a la variable
        this.idModelo = this.$route.params.id;
    },
    methods: {
        crearParte() {
            const requestBody = {
                nombre: this.nombre,
                idModelo: this.idModelo 
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
                else{
                    console.log("Parte creado");
                };
                // Redirigir a /Partes
                this.$router.push(`/modelos/${this.idModelo}`);
            }).catch(error => {
                console.error(error);
            });
        }
    }
}
</script>
