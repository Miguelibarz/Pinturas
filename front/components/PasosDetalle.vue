<template>
    <v-card class="pa-2">
        <v-card-title class="detalles">{{ capitalizeFirst(pasos?.nombre) }}</v-card-title>
        <v-row class="d-flex pa-4 align-center d-flex">
            <v-col cols="1" class="color-square pa-2"
                :style="{ backgroundColor: color?.codigoHex + ' !important' }"></v-col>
            <v-col >{{ capitalizeFirst(color?.nombre) }}</v-col>
            <v-col >{{ capitalizeFirst(pasos?.comentario) }}</v-col>
            <v-col cols="2">
                <v-btn v-if="pasos" :to="`../modify/paso/${pasos.id}`" color="info">
                    <v-icon>mdi-pencil</v-icon>
                </v-btn>
                <v-btn @click="deletePaso" color="error">
                    <v-icon>mdi-delete</v-icon>
                </v-btn>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
export default {
    props: {
        pasos: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            color: null
        };
    },
    async mounted() {
        await this.getColor(this.pasos.idColor);
    },
    methods: {
        async getColor(colorId) {
            try {
                const response = await fetch(`${process.env.API_URL}/colores/${colorId}`);
                const data = await response.json();
                this.color = data;
            } catch (error) {
                console.error('Error fetching color:', error);
            }
        },
        async deletePaso() {
            try {
                const response = await fetch(`${process.env.API_URL}/pasos/${this.pasos.id}`, {
                    method: 'DELETE'
                });
                window.location.reload()

                if (!response.ok) {
                    throw new Error('Failed to delete paso');
                }
                this.$emit('pasoDeleted', this.pasos.id);
            } catch (error) {
                console.error('Error deleting paso:', error);
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
.color-square {
    width: 40px;
    height: 40px;
    margin-left: 10px;
}
</style>