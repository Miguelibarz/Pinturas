<template>
    <div>
        <v-row>
            <v-col cols="12">
                <v-card-title class="text-h4">Lista de Colores</v-card-title>
            </v-col>
            <v-col>
                <v-color-picker :hide-mode-switch="false" swatches-max-height="400px" show-swatches v-model="color"
                    mode="hexa"></v-color-picker>
            </v-col>
        </v-row>

    </div>
</template>

<script>
import ColorDetalle from '@/components/ColorDetalle.vue'; // Asegúrate de tener la ruta correcta hacia el componente

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
        }
    }
};
</script>
<style>


</style>