<template>
    <v-col cols="4">
        <v-card class="pa-4">
            <router-link :to="'/partes/' + parte.id" class="enlace">
                <img v-if="parte.imagen" :src="`/images/${parte.imagen}`" style="width: 100%;">
                <v-card-title class="no-underline pa-0">{{ capitalizeFirst(parte.nombre) }}
                </v-card-title>
            </router-link>
        </v-card>
    </v-col>
</template>

<script>
export default {
    props: {
        parte: {
            type: Object,
            required: true
        }
    },
    methods: {
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
    color: #fff;
}

.enlace:hover {
    color: #dadada
}
</style>
