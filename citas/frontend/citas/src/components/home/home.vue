<template>
    <div>
        <Search />
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="i in factura">
            <CardFactura :i={...i} />
        </template>
    </div>
</template>

<script lang="ts" >
import { store } from '../../context/store';
import CardFactura from '../UI/card.vue';
import verfactura from '../factura/ver/verfactura.vue';
import Search from '../UI/search.vue';

export default {
    data() {
        return {
            factura: [...store.state.factura]
        }
    },
    mounted() {
        store.commit('getAllFactura', "http://127.0.0.1:8000/facturas/fall/")
    },
    components: {
        Search,
        verfactura,
        CardFactura
    },
}
</script>

<style scoped lang="scss">

</style>