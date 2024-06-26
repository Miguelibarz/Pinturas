<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-text-field v-model="search" label="Buscar" solo-inverted></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10">
        <v-card-title class="text-h4">Lista de Modelos</v-card-title>
      </v-col>
      <v-col cols="2" class="d-flex justify-end align-center pa-6">
        <v-btn to="Add/modelo">
          <v-icon>mdi-plus</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-container>
      <!-- Agregar una lista de ModeloDetalle aquí -->
      <div v-if="modelos.length === 0">No hay modelos disponibles</div>
      <v-row v-else>
        <ModeloDetalle v-for="(modelo, index) in modelos" :key="index" :modelo="modelo" />
      </v-row>
    </v-container>
    <!-- Botón para pasar a la siguiente página -->
    <v-btn v-if="currentPage < totalPages" @click="fetchNextPage">Cargar mas</v-btn>
  </div>
</template>

<script>
import ModeloDetalle from '../components/ModeloDetalle.vue';

export default {
  components: {
    ModeloDetalle,
  },
  data() {
    return {
      modelos: [],
      currentPage: 1,
      perPage: 10,
      totalItems: 0,
      loading: false,
      search: '', 
    };
  },
  watch: {
    search(newSearch) {
      this.currentPage = 1; 
      this.modelos = []; 
      this.fetchModelos(); 
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalItems / this.perPage);
    }
  },
  mounted() {
    this.fetchModelos();
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    async fetchModelos() {
      try {
        if (this.loading) return; // Avoid multiple simultaneous requests
        this.loading = true;

        const response = await fetch(`${process.env.API_URL}/search_modelo?search=${this.search}&skip=${(this.currentPage - 1) * this.perPage}&limit=${this.perPage}`);
        const data = await response.json();
        this.modelos.push(...data);

        this.loading = false;

        // Obtener el total de modelos para la paginación
        const totalResponse = await fetch(`${process.env.API_URL}/modelos/count`);
        const totalData = await totalResponse.json();
        this.totalItems = totalData.count;
      } catch (error) {
        console.error('Error fetching modelos:', error);
        this.loading = false;
      }
    },
    async fetchNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        await this.fetchModelos();
      }
    },
    handleScroll() {
      const bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
      if (bottomOfWindow) {
        this.currentPage++;
        this.fetchModelos();
      }
    }
  }
};
</script>
