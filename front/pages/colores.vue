<template>
  <div>
    <v-row>
      <v-col cols="12">
        <v-text-field v-model="search" label="Buscar" solo-inverted></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="10">
        <v-card-title class="text-h4">Lista de colores</v-card-title>
      </v-col>
      <v-col cols="2" class="d-flex justify-end align-center pa-6">
        <v-btn @click="importColores">
          <v-icon>mdi-plus</v-icon>
          Importar desde fichero
        </v-btn>
      </v-col>
    </v-row>
    <v-container>
      <div v-if="colores.length === 0">No hay colores disponibles</div>
      <v-row v-else>
        <ColorDetalle v-for="(color, index) in colores" :key="index" :color="color" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import ColorDetalle from '@/components/ColorDetalle.vue'; 

export default {
  components: {
    ColorDetalle,
  },
  data() {
    return {
      colores: [],
      search: '', 
      currentPage: 1,
      perPage: 12,
      totalItems: 0,
      loading: false,
    };
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalItems / this.perPage);
    }
  },
  watch: {
    search(newSearch) {
      this.currentPage = 1; 
      this.colores = []; 
      this.fetchColores(); 
    }
  },
  mounted() {
    this.fetchColores();
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    async fetchColores() {
      try {
        if (this.loading) return;
        this.loading = true;

        const response = await fetch(`${process.env.API_URL}/search_colores?search=${this.search}&skip=${(this.currentPage - 1) * this.perPage}&limit=${this.perPage}`);
        const data = await response.json();
        this.colores.push(...data);
        this.loading = false;
      } catch (error) {
        console.error('Error fetching colores:', error);
        this.loading = false;
      }
    },
    async importColores() {
      try {
        const response = await fetch(`${process.env.API_URL}/import-colores/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
        });
        const data = await response.json();
        this.colores = data;
      } catch (error) {
        console.error('Error importing colores:', error);
      }
    },
    async fetchNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        await this.fetchColores();
      }
    },
    handleScroll() {
      const bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
      if (bottomOfWindow) {
        this.currentPage++;
        this.fetchColores();
      }
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.totalItems / this.perPage);
    }
  }
};
</script>

<style scoped>
.v-card {
  cursor: pointer;
  transition: transform 0.3s;
}

.v-card:hover {
  transform: scale(1.05);
}
</style>
