<template>
    <v-col cols="4">
        <v-card class="pa-4">
            <router-link :to="'/partes/' + parte.id" class="enlace">
                <img v-if="parte.imagen" :src="`/images/${parte.imagen}`" style="width: 100%;">
                <v-card-title class="no-underline pa-0">
                    {{ capitalizeFirst(parte.nombre) }}
                </v-card-title>
                <router-link v-if="isPartesRoute && modelo" :to="'/modelos/' + parte.idModelo"
                class="enlace enlace-modelo">
                    {{ capitalizeFirst(modelo.nombre) }}
                </router-link>
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
    data() {
        return {
            modelo: null
        };
    },
    methods: {
        async fetchModelo() {
            try {
                const response = await fetch(process.env.API_URL + `/modelos/${this.parte.idModelo}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch modelo');
                }
                this.modelo = await response.json();
            } catch (error) {
                console.error(error);
            }
        },
        capitalizeFirst(text) {
            if (!text) return '';
            return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
        }
    },
    computed: {
        isPartesRoute() {
            return this.$route.path === '/partes';
        }
    },
    created() {
        if (this.isPartesRoute) {
            this.fetchModelo();
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
.enlace.enlace-modelo:hover{
    font-size: 20px;
    color: #b9e9ff;
    transition: font-size 0.2s;
}
</style>
