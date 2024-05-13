<template>
    <v-col cols="4">
        <v-card class="pa-4">
            <router-link :to="'/partes/' + parte.id">
                <v-card-title>{{ capitalize(parte.nombre) }}</v-card-title>
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
        capitalize(string) {
            return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
        }
    }
};
</script>

<style scoped></style>
