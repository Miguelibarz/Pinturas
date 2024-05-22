<template>
    <div>
      <v-row>
        <v-col cols="10">
          <v-card-title class="text-h4">Lista de partes</v-card-title>
        </v-col>
        <v-col cols="2" class="d-flex justify-end align-center pa-6">
          <!-- <v-btn to="Add/parte" >
            <v-icon>mdi-plus</v-icon>
          </v-btn> -->
        </v-col>
      </v-row>
      <v-container>
        <!-- Agregar una lista de parteDetalle aquí -->
        <div v-if="partes.length === 0">No hay partes disponibles</div>
        <v-row v-else>
          <parteDetalle v-for="(parte, index) in partes" :key="index" :parte="parte" />
        </v-row>
      </v-container>
      <!-- Botón para pasar a la siguiente página -->
      <v-btn v-if="currentPage < totalPages" @click="fetchNextPage">Cargar mas</v-btn>
    </div>
  </template>
  
  <script>
  import parteDetalle from '../components/TarjetaParte.vue';
  
  export default {
    components: {
      parteDetalle,
    },
    data() {
      return {
        partes: [],
        currentPage: 1,
        perPage: 10,
        totalItems: 0,
        loading: false,
      };
    },
    computed: {
      totalPages() {
        return Math.ceil(this.totalItems / this.perPage);
      }
    },
    mounted() {
      this.fetchpartes();
      window.addEventListener('scroll', this.handleScroll);
    },
    beforeDestroy() {
      window.removeEventListener('scroll', this.handleScroll);
    },
    methods: {
      async fetchpartes() {
        try {
          if (this.loading) return; // Avoid multiple simultaneous requests
          this.loading = true;
  
          const response = await fetch(`${process.env.API_URL}/partes?skip=${(this.currentPage - 1) * this.perPage}&limit=${this.perPage}`);
          const data = await response.json();
          this.partes.push(...data);
          this.loading = false;
  
          // Opcional: Obtener el total de partes para la paginación
          const totalResponse = await fetch(`${process.env.API_URL}/partes/count`);
          const totalData = await totalResponse.json();
          this.totalItems = totalData.count;
        } catch (error) {
          console.error('Error fetching partes:', error);
          this.loading = false;
        }
      },
      async fetchNextPage() {
        if (this.currentPage < this.totalPages) {
          this.currentPage++;
          await this.fetchpartes();
        }
      },
      handleScroll() {
        const bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.currentPage++;
          this.fetchpartes();
        }
      }
    }
  };
  </script>
  